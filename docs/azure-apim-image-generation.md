# Generating images through the `pingpingapim` Azure APIM gateway

This note captures how the dashboard's UI-mockup workflow creates and edits
images through an Azure API Management (APIM) gateway that fronts Azure
OpenAI `gpt-image-*` deployments. It is distilled from two existing
implementations:

- `…/Dashboard/ui_mockups/scripts/generate_mockups.py` + `common.py` (Python)
- `C:\dev\vscode\Invoke-PingPingApimImage.ps1` (standalone PowerShell)

A working, self-contained Python port lives at
[`scripts/generate_image_apim.py`](../scripts/generate_image_apim.py).

> Secrets are **not** stored in this repo. The script reads the APIM
> subscription key from an environment variable (or `.env`) at runtime.

## Gateway shape

```
Base URL : https://pingpingapim.azure-api.net
Auth     : header  api-key: <APIM subscription key>
Path     : /openai/deployments/{deployment}/images/{operation}
Query    : ?api-version=2025-04-01-preview
```

- `deployment` — the Azure OpenAI image model deployment behind APIM.
  Defaults: `gpt-image-2` for opaque output, `gpt-image-1.5` when a
  transparent background is required.
- `operation` — `generations` for prompt-to-image, `edits` for
  image-to-image.

The same `api-key` header works for both routes. No bearer token, AAD
exchange, or `Authorization` header is involved at this layer — APIM
injects the upstream Azure OpenAI auth itself.

### Environment variables

Two values are required. Names follow the existing dashboard convention
so the same `.env` works across tools:

| Variable                          | Purpose                                                                 |
| --------------------------------- | ----------------------------------------------------------------------- |
| `PINGAPIM_GATEWAY_URL`            | Base gateway URL, e.g. `https://pingpingapim.azure-api.net`             |
| `PINGPINGAPIM_SUBSCRIPTION_KEY`   | APIM subscription key sent as the `api-key` header                      |

Optional:

| Variable                           | Purpose                                                                |
| ---------------------------------- | ---------------------------------------------------------------------- |
| `UI_MOCKUPS_IMAGE_MODEL`           | Override the deployment name (defaults to `gpt-image-2`)               |
| `UI_MOCKUPS_TRANSPARENT_BACKGROUND`| `true`/`1`/`yes` swaps the default deployment to `gpt-image-1.5`       |

## Operation 1 — text-to-image (`/images/generations`)

`POST {gateway}/openai/deployments/{deployment}/images/generations?api-version=2025-04-01-preview`

- `Content-Type: application/json`
- Body (subset of Azure OpenAI's GPT-image schema):

```json
{
  "model": "gpt-image-2",
  "prompt": "A cinematic product photo of a glass robot on a workbench",
  "size": "2880x2880",
  "n": 1,
  "quality": "high",
  "output_format": "png"
}
```

Optional body fields used by the existing scripts:

- `output_compression` — integer 0–100, only when `output_format=jpeg`.
- `user` — non-secret identifier for monitoring / abuse detection.

### Size, quality, orientation

GPT-image-2 enforces these constraints (validated by the PowerShell helper):

- Both edges divisible by 16.
- Long edge ≤ 3840 px.
- Aspect ratio ≤ 3:1.
- Total pixels between 655,360 and 8,294,400.

Largest pixel-count presets per orientation:

| Orientation | Size        | Pixels    |
| ----------- | ----------- | --------- |
| Square      | 2880×2880   | 8,294,400 |
| Landscape   | 3840×2160   | 8,294,400 |
| Portrait    | 2160×3840   | 8,294,400 |

Allowed `quality` values: `low`, `medium`, `high` (lower-case in the
request body).

## Operation 2 — image-to-image (`/images/edits`)

`POST {gateway}/openai/deployments/{deployment}/images/edits?api-version=2025-04-01-preview`

- `Content-Type: multipart/form-data` (do **not** set this header
  manually when using `requests`; let it set the boundary).
- Form fields:

| Field            | Required | Notes                                                                |
| ---------------- | -------- | -------------------------------------------------------------------- |
| `image[]`        | yes      | One or more PNG/JPEG files; the field name uses the literal `[]`.    |
| `prompt`         | yes      | Natural-language edit instruction.                                   |
| `model`          | yes      | Deployment name (matches the URL).                                   |
| `size`           | yes      | Same constraints as generation; the mockup workflow uses `1536x1024`.|
| `n`              | yes      | Number of variants. The mockup workflow always uses `1`.             |
| `background`     | no       | `transparent` to request a transparent PNG (needs `gpt-image-1.5`).  |
| `input_fidelity` | no       | `low` or `high`; higher preserves more of the input image.           |

## Response shape

Both routes return JSON of the form:

```json
{
  "created": 1717080000,
  "data": [
    { "b64_json": "<base64-encoded PNG/JPEG bytes>" }
  ]
}
```

Decode each `data[i].b64_json` value with standard base64 and write the
bytes to disk. There is no streaming and no separate download URL; the
image is inline.

## Timeouts and limits

- APIM's practical maximum request lifetime is around **240 seconds**.
  The PowerShell helper caps `TimeoutSeconds` at 240 for that reason.
- Python callers that batch many edits in one process (the mockup
  workflow) use a longer client-side socket timeout (600–900 s) only to
  tolerate retries and network jitter — the gateway itself still cuts
  off at ~240 s per request.

## Minimal Python skeleton

```python
import base64, os, requests

gateway = os.environ["PINGAPIM_GATEWAY_URL"].rstrip("/")
key     = os.environ["PINGPINGAPIM_SUBSCRIPTION_KEY"]
model   = "gpt-image-2"
url     = f"{gateway}/openai/deployments/{model}/images/generations?api-version=2025-04-01-preview"

response = requests.post(
    url,
    headers={"api-key": key, "Content-Type": "application/json"},
    json={
        "model": model,
        "prompt": "A cinematic product photo of a glass robot on a workbench",
        "size": "2880x2880",
        "n": 1,
        "quality": "high",
        "output_format": "png",
    },
    timeout=240,
)
response.raise_for_status()
payload = response.json()

with open("out.png", "wb") as handle:
    handle.write(base64.b64decode(payload["data"][0]["b64_json"]))
```

For the edit route, swap `images/generations` for `images/edits`, drop
the JSON body, and post a `multipart/form-data` payload whose `image[]`
field contains the input file.

## Where to look in the source

- `…/ui_mockups/scripts/common.py` — env loading, `api-key` header,
  base64 helpers, multipart `image[]` upload.
- `…/ui_mockups/scripts/generate_mockups.py` — full edit flow, including
  the `/images/edits` route and the response → `b64_json` decoding.
- `C:\dev\vscode\Invoke-PingPingApimImage.ps1` — standalone PowerShell
  implementation with explicit GPT-image-2 size validation.
