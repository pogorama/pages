"""Generate or edit an image through the `pingpingapim` Azure APIM gateway.

This is a self-contained Python port of two existing helpers:

- `…/Dashboard/ui_mockups/scripts/generate_mockups.py` + `common.py`
- `C:\\dev\\vscode\\Invoke-PingPingApimImage.ps1`

It calls the Azure OpenAI GPT-image image generation/edit APIs through
the public APIM gateway at `https://pingpingapim.azure-api.net`. See
`docs/azure-apim-image-generation.md` for the full protocol description.

Secrets:
    The APIM subscription key is read from the
    `PINGPINGAPIM_SUBSCRIPTION_KEY` environment variable, or from a
    `.env` file. No key is ever read from or written to this script.

    On this workstation the key currently lives at::

        C:\\Users\\phgermey\\OneDrive - Microsoft\\###AO\\Dashboard\\ui_mockups\\.env

    The script auto-discovers that path (see ``KNOWN_ENV_FILE_PATHS``
    below) and falls back to it whenever the repo-root ``.env`` does
    not exist. If you need to point at a different ``.env``, pass
    ``--env-file <path>`` explicitly.

Examples (PowerShell):

    # No env setup needed — the script auto-discovers the dashboard .env.
    python .\\scripts\\generate_image_apim.py `
        --prompt "A cinematic product photo of a glass robot on a workbench" `
        --output-dir .\\out

    # Explicit env file override.
    python .\\scripts\\generate_image_apim.py `
        --env-file "C:\\Users\\phgermey\\OneDrive - Microsoft\\###AO\\Dashboard\\ui_mockups\\.env" `
        --prompt "Change the paperclip to a Peruvian paperclip in watercolor." `
        --edit-image .\\inputs\\original.png `
        --output-dir .\\out `
        --quality low
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import email.utils
import json
import mimetypes
import os
import random
import re
import sys
import time
from pathlib import Path
from typing import Any

import urllib.request
import urllib.error
import uuid


DEFAULT_GATEWAY_URL = "https://pingpingapim.azure-api.net"
DEFAULT_DEPLOYMENT = "gpt-image-2"
TRANSPARENT_DEPLOYMENT = "gpt-image-1.5"
DEFAULT_API_VERSION = "2025-04-01-preview"
DEFAULT_TIMEOUT_SECONDS = 240

# Where the APIM subscription key actually lives on this workstation.
# Searched in order; the first existing file wins. --env-file overrides
# all of these. Adding a path here is the right way to "remember" a new
# location across runs.
KNOWN_ENV_FILE_PATHS: list[Path] = [
    # 1. Repo-root .env (preferred for new setups).
    Path(__file__).resolve().parent.parent / ".env",
    # 2. Existing dashboard configuration. This is where the
    #    PINGPINGAPIM_SUBSCRIPTION_KEY currently lives and has lived for
    #    the entire pogorama/pages project. If the script ever reports
    #    "Missing APIM subscription key", check that this path still
    #    exists before suggesting the user set an env var.
    Path(
        r"C:\Users\phgermey\OneDrive - Microsoft\###AO\Dashboard\ui_mockups\.env"
    ),
    # 3. Shared LiteLLM-style .env at C:\dev\vscode (kept for parity
    #    even though it currently does NOT contain the PINGPINGAPIM key).
    Path(r"C:\dev\vscode\.env"),
]


def find_default_env_file() -> Path | None:
    """Return the first KNOWN_ENV_FILE_PATHS entry that exists, or None."""
    for candidate in KNOWN_ENV_FILE_PATHS:
        try:
            if candidate.exists():
                return candidate
        except OSError:
            continue
    return None


ORIENTATION_PRESETS = {
    "square": "2880x2880",
    "landscape": "3840x2160",
    "portrait": "2160x3840",
}

VALID_QUALITY = {"low", "medium", "high"}
VALID_OUTPUT_FORMATS = {"png", "jpeg"}


def parse_env_file(path: Path) -> dict[str, str]:
    """Parse a trivial KEY=VALUE .env file. Missing files are tolerated."""
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def parse_bool(value: str | None) -> bool:
    return value is not None and value.strip().lower() in {"1", "true", "yes", "on"}


def resolve_config(args: argparse.Namespace) -> dict[str, str]:
    """Merge command-line args, OS env, and an optional .env file."""
    if args.env_file:
        env_path = Path(args.env_file)
    else:
        discovered = find_default_env_file()
        env_path = discovered if discovered is not None else (
            Path(__file__).resolve().parent.parent / ".env"
        )
    env_file = parse_env_file(env_path)

    def pick(env_name: str, cli_value: str | None, fallback: str | None = None) -> str | None:
        return cli_value or os.environ.get(env_name) or env_file.get(env_name) or fallback

    transparent = (
        args.transparent_background
        or parse_bool(os.environ.get("UI_MOCKUPS_TRANSPARENT_BACKGROUND"))
        or parse_bool(env_file.get("UI_MOCKUPS_TRANSPARENT_BACKGROUND"))
    )

    deployment = pick(
        "UI_MOCKUPS_IMAGE_MODEL",
        args.deployment,
        TRANSPARENT_DEPLOYMENT if transparent else DEFAULT_DEPLOYMENT,
    )

    gateway = pick("PINGAPIM_GATEWAY_URL", args.gateway_url, DEFAULT_GATEWAY_URL)
    key = pick("PINGPINGAPIM_SUBSCRIPTION_KEY", args.api_key)

    if not key:
        searched = "\n  - ".join(str(p) for p in KNOWN_ENV_FILE_PATHS)
        raise SystemExit(
            "Missing APIM subscription key (PINGPINGAPIM_SUBSCRIPTION_KEY).\n"
            f"Auto-discovery searched these .env paths in order:\n  - {searched}\n"
            "None of them contained the key. Either:\n"
            "  1. add PINGPINGAPIM_SUBSCRIPTION_KEY=... to one of them,\n"
            "  2. pass --env-file <path>, or\n"
            "  3. pass --api-key <key>.\n"
            "(No keys are read from or written to this script.)"
        )

    return {
        "gateway": gateway.rstrip("/"),
        "api_key": key,
        "deployment": deployment,
        "api_version": args.api_version,
        "transparent": "true" if transparent else "",
    }


def resolve_size(args: argparse.Namespace) -> str:
    if args.size:
        validate_size(args.size)
        return args.size
    return ORIENTATION_PRESETS[args.orientation]


def validate_size(size: str) -> None:
    """Mirror the GPT-image-2 constraints used by the PowerShell helper."""
    match = re.fullmatch(r"\s*(\d+)\s*[xX*]\s*(\d+)\s*", size)
    if not match:
        raise SystemExit("--size must use WIDTHxHEIGHT (e.g. 1024x1024).")
    width, height = int(match.group(1)), int(match.group(2))
    if width <= 0 or height <= 0:
        raise SystemExit("--size dimensions must be positive.")
    if width % 16 or height % 16:
        raise SystemExit("GPT-image-2 requires both edges to be divisible by 16.")
    if max(width, height) > 3840:
        raise SystemExit("GPT-image-2 long edge must be 3840 px or less.")
    if max(width, height) / min(width, height) > 3:
        raise SystemExit("GPT-image-2 aspect ratio must be 3:1 or less.")
    pixels = width * height
    if pixels < 655_360 or pixels > 8_294_400:
        raise SystemExit("GPT-image-2 total pixels must be between 655,360 and 8,294,400.")


def build_url(config: dict[str, str], operation: str) -> str:
    return (
        f"{config['gateway']}/openai/deployments/{config['deployment']}/images/"
        f"{operation}?api-version={config['api_version']}"
    )


def _parse_retry_after(header_value: str | None) -> float | None:
    """Parse RFC 7231 Retry-After: either an int (seconds) or HTTP-date."""
    if not header_value:
        return None
    header_value = header_value.strip()
    try:
        # Integer seconds form
        return max(0.0, float(header_value))
    except ValueError:
        pass
    # HTTP-date form
    try:
        when = email.utils.parsedate_to_datetime(header_value)
        if when is None:
            return None
        now = dt.datetime.now(dt.timezone.utc)
        if when.tzinfo is None:
            when = when.replace(tzinfo=dt.timezone.utc)
        return max(0.0, (when - now).total_seconds())
    except Exception:
        return None


# HTTP status codes that are worth retrying.
# 408 request timeout, 425 too early, 429 rate-limited / engine overloaded,
# 500 internal, 502 bad gateway, 503 service unavailable, 504 gateway timeout.
_RETRYABLE_STATUS = {408, 425, 429, 500, 502, 503, 504}

# Default backoff schedule when Retry-After is not supplied.
# Image RPM at Tier 1 is ~9 RPM (gpt-image-2 GlobalStandard) — ~7s/req.
# Use 8s base, doubling, capped at 60s, plus jitter.
# Reference: https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits
_BACKOFF_BASE_SECONDS = 8.0
_BACKOFF_CAP_SECONDS = 60.0
_DEFAULT_MAX_ATTEMPTS = 4

# Hard upper bound on --max-attempts. Anything higher is rejected at the
# CLI. Retrying 40 times against an "EngineOverloaded" or "503" backend
# does not fix the underlying problem; it just wastes wall time and
# hides the real Azure error from the operator.
_HARD_MAX_ATTEMPTS = 6

# Total wall-time budget for one image generation call, including all
# retry sleeps. If the budget is exhausted, the script aborts with the
# most recent Azure response body so the operator can act on the real
# error (engine overload, bad prompt, expired key, quota exceeded, …).
# User requirement: "image creation should not take longer than 3
# minutes, never. if so then there is an error."
_TOTAL_DEADLINE_SECONDS = 180.0


def http_post(
    url: str,
    api_key: str,
    *,
    json_body: dict[str, Any] | None = None,
    multipart: tuple[dict[str, str], list[tuple[str, Path]]] | None = None,
    timeout: int = DEFAULT_TIMEOUT_SECONDS,
    max_attempts: int = _DEFAULT_MAX_ATTEMPTS,
    total_deadline_seconds: float = _TOTAL_DEADLINE_SECONDS,
) -> dict[str, Any]:
    """POST JSON or multipart/form-data via the stdlib, return parsed JSON.

    Retries automatically on transient errors (HTTP 408/425/429/5xx and
    connection/timeout errors). When the server provides a Retry-After
    header it is respected. Otherwise an exponential backoff with jitter
    is used, capped at ``_BACKOFF_CAP_SECONDS``.

    Hard limits:
      - ``max_attempts`` is capped at ``_HARD_MAX_ATTEMPTS``.
      - Total wall time (request + every sleep) is capped at
        ``total_deadline_seconds``. If the next planned sleep would
        exceed the budget, the script aborts immediately and surfaces
        the most recent Azure response body so the operator can act on
        the real error.

    See Azure OpenAI quotas-and-limits docs and Microsoft Learn
    "Error codes" reference.
    """
    if (json_body is None) == (multipart is None):
        raise ValueError("Provide exactly one of json_body or multipart.")

    # Clamp max_attempts defensively even though argparse also clamps.
    max_attempts = max(1, min(max_attempts, _HARD_MAX_ATTEMPTS))

    base_headers = {
        "api-key": api_key,
        "User-Agent": "pogorama-pages-apim-image/1.0",
    }

    if json_body is not None:
        body_data = json.dumps(json_body).encode("utf-8")
        body_content_type = "application/json"
        encoded_multipart_args: tuple[Any, Any] | None = None
    else:
        fields, files = multipart
        boundary = f"----pogoramaBoundary{uuid.uuid4().hex}"
        body_content_type = f"multipart/form-data; boundary={boundary}"
        body_data = encode_multipart(fields, files, boundary)
        encoded_multipart_args = (fields, files)
    # Suppress unused-variable warnings for the multipart capture (kept for
    # future per-attempt re-encoding if file streams ever become consumable).
    del encoded_multipart_args

    started_at = time.monotonic()
    deadline_at = started_at + total_deadline_seconds

    last_error_detail: str | None = None
    last_status: int | None = None
    last_reason: str | None = None

    def _abort_with_azure_error(reason_prefix: str) -> "SystemExit":
        elapsed = time.monotonic() - started_at
        status_part = (
            f"{last_status} {last_reason}" if last_status is not None
            else "no HTTP status (connection error)"
        )
        return SystemExit(
            f"{reason_prefix} after {elapsed:.0f}s. "
            f"Last Azure response: {status_part}\n"
            f"Body:\n{last_error_detail or '(no body captured)'}\n"
            f"\nThis is a real upstream error, not a retry-budget bug. "
            f"Investigate the body above before re-running. Common causes:\n"
            f"  - EngineOverloaded / 503: Azure capacity throttling; "
            f"try again in a few minutes or switch deployment region.\n"
            f"  - 429: subscription quota exceeded; check quotas in the "
            f"Azure portal.\n"
            f"  - 400: prompt rejected (content filter, size, schema).\n"
            f"  - 401/403: APIM subscription key invalid or revoked."
        )

    for attempt in range(1, max_attempts + 1):
        headers = dict(base_headers)
        headers["Content-Type"] = body_content_type
        request = urllib.request.Request(
            url, data=body_data, headers=headers, method="POST"
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                body = response.read()
            try:
                return json.loads(body.decode("utf-8"))
            except json.JSONDecodeError as error:
                raise SystemExit(
                    f"APIM returned non-JSON response: {body[:500]!r}"
                ) from error
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")
            last_error_detail = detail
            last_status = error.code
            last_reason = error.reason
            status = error.code
            if status not in _RETRYABLE_STATUS or attempt == max_attempts:
                raise SystemExit(
                    f"APIM call failed ({status} {error.reason}): {detail}"
                ) from error

            retry_after_hdr = (
                error.headers.get("Retry-After") if error.headers else None
            )
            wait_seconds = _parse_retry_after(retry_after_hdr)
            if wait_seconds is None:
                # Exponential backoff with full jitter, capped.
                wait_seconds = min(
                    _BACKOFF_CAP_SECONDS,
                    _BACKOFF_BASE_SECONDS * (2 ** (attempt - 1)),
                )
                wait_seconds *= 0.5 + random.random() * 0.5
            else:
                # Always cap server-suggested waits at the backoff ceiling.
                wait_seconds = min(wait_seconds, _BACKOFF_CAP_SECONDS)

            remaining = deadline_at - time.monotonic()
            if wait_seconds >= remaining or remaining < 1.0:
                raise _abort_with_azure_error(
                    f"Aborting: Azure-suggested wait ({wait_seconds:.0f}s) "
                    f"exceeds remaining budget ({max(0.0, remaining):.0f}s) "
                    f"after {attempt} attempt(s)"
                )

            print(
                f"[retry {attempt}/{max_attempts - 1}] APIM returned {status} "
                f"{error.reason}; sleeping {wait_seconds:.1f}s before retry "
                f"(deadline in {remaining:.0f}s). "
                f"(detail: {detail[:160]}...)",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(wait_seconds)
            continue
        except urllib.error.URLError as error:
            last_error_detail = str(error)
            last_status = None
            last_reason = None
            if attempt == max_attempts:
                raise SystemExit(f"APIM call failed: {error}") from error
            wait_seconds = min(
                _BACKOFF_CAP_SECONDS,
                _BACKOFF_BASE_SECONDS * (2 ** (attempt - 1)),
            ) * (0.5 + random.random() * 0.5)

            remaining = deadline_at - time.monotonic()
            if wait_seconds >= remaining or remaining < 1.0:
                raise _abort_with_azure_error(
                    f"Aborting: backoff sleep ({wait_seconds:.0f}s) exceeds "
                    f"remaining budget ({max(0.0, remaining):.0f}s) "
                    f"after {attempt} attempt(s)"
                )

            print(
                f"[retry {attempt}/{max_attempts - 1}] Connection error "
                f"({error}); sleeping {wait_seconds:.1f}s before retry "
                f"(deadline in {remaining:.0f}s).",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(wait_seconds)
            continue

    raise _abort_with_azure_error(
        f"APIM call exhausted {max_attempts} attempt(s)"
    )


def encode_multipart(
    fields: dict[str, str],
    files: list[tuple[str, Path]],
    boundary: str,
) -> bytes:
    """Encode fields and files as multipart/form-data."""
    chunks: list[bytes] = []
    for name, value in fields.items():
        chunks.append(f"--{boundary}\r\n".encode())
        chunks.append(
            f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode()
        )
        chunks.append(str(value).encode("utf-8"))
        chunks.append(b"\r\n")

    for field_name, file_path in files:
        content_type = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"
        chunks.append(f"--{boundary}\r\n".encode())
        chunks.append(
            (
                f'Content-Disposition: form-data; name="{field_name}"; '
                f'filename="{file_path.name}"\r\n'
                f"Content-Type: {content_type}\r\n\r\n"
            ).encode()
        )
        chunks.append(file_path.read_bytes())
        chunks.append(b"\r\n")

    chunks.append(f"--{boundary}--\r\n".encode())
    return b"".join(chunks)


def save_images(payload: dict[str, Any], output_dir: Path, extension: str) -> list[dict[str, Any]]:
    if "data" not in payload or not isinstance(payload["data"], list):
        raise SystemExit(f"Response had no 'data' array: {json.dumps(payload)[:500]}")

    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")
    saved: list[dict[str, Any]] = []

    for index, item in enumerate(payload["data"], start=1):
        b64 = item.get("b64_json")
        if not b64:
            raise SystemExit(f"Response item #{index} missing 'b64_json'.")
        base_name = f"{timestamp}-imager" if index == 1 else f"{timestamp}-imager-{index:02d}"
        file_path = output_dir / f"{base_name}.{extension}"
        file_bytes = base64.b64decode(b64)
        file_path.write_bytes(file_bytes)
        saved.append(
            {
                "index": index,
                "path": str(file_path.resolve()),
                "bytes": len(file_bytes),
            }
        )
    return saved


def sanitize_response(payload: dict[str, Any]) -> dict[str, Any]:
    """Return a copy with the long base64 image fields replaced by a length marker."""
    copy = json.loads(json.dumps(payload))
    for item in copy.get("data", []) or []:
        if isinstance(item, dict) and item.get("b64_json"):
            item["b64_json_length"] = len(item["b64_json"])
            item["b64_json_omitted"] = True
            del item["b64_json"]
    return copy


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate or edit an image through the pingpingapim Azure APIM gateway.",
    )
    parser.add_argument("--prompt", required=True, help="Natural-language prompt or edit instruction.")
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Folder where the generated/edited image(s) will be saved.",
    )
    parser.add_argument(
        "--edit-image",
        help="Path to an existing PNG/JPEG. When supplied, the script calls /images/edits.",
    )
    parser.add_argument(
        "--orientation",
        choices=sorted(ORIENTATION_PRESETS),
        default="square",
        help="Selects the largest preset size for that orientation (ignored if --size is set).",
    )
    parser.add_argument(
        "--size",
        help="Explicit WIDTHxHEIGHT (must satisfy GPT-image-2 constraints).",
    )
    parser.add_argument(
        "--quality",
        choices=sorted(VALID_QUALITY),
        default="high",
    )
    parser.add_argument("--count", "-n", type=int, default=1, help="Number of images to request (1–10).")
    parser.add_argument(
        "--output-format",
        choices=sorted(VALID_OUTPUT_FORMATS),
        default="png",
    )
    parser.add_argument(
        "--output-compression",
        type=int,
        help="JPEG compression 0–100; only meaningful when --output-format=jpeg.",
    )
    parser.add_argument(
        "--input-fidelity",
        choices=["low", "high"],
        default="high",
        help="Edit-only: how strongly the input image should be preserved.",
    )
    parser.add_argument(
        "--transparent-background",
        action="store_true",
        help="Request a transparent PNG (switches default deployment to gpt-image-1.5).",
    )
    parser.add_argument("--deployment", help=f"Override deployment name (default {DEFAULT_DEPLOYMENT}).")
    parser.add_argument("--gateway-url", help=f"Override gateway URL (default {DEFAULT_GATEWAY_URL}).")
    parser.add_argument("--api-version", default=DEFAULT_API_VERSION)
    parser.add_argument("--api-key", help="APIM subscription key (prefer the env var).")
    parser.add_argument(
        "--env-file",
        help="Path to a .env file with PINGAPIM_GATEWAY_URL / PINGPINGAPIM_SUBSCRIPTION_KEY.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT_SECONDS,
        help="Client-side socket timeout in seconds (APIM caps at ~240).",
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=_DEFAULT_MAX_ATTEMPTS,
        help=(
            "Maximum HTTP attempts (initial + retries) on transient errors "
            "(429 / 5xx / connection errors). The script respects "
            "Retry-After if present, otherwise uses exponential backoff "
            f"with jitter (base {int(_BACKOFF_BASE_SECONDS)}s, "
            f"cap {int(_BACKOFF_CAP_SECONDS)}s). "
            f"Hard upper bound: {_HARD_MAX_ATTEMPTS}. "
            f"Total wall time is also capped at "
            f"{int(_TOTAL_DEADLINE_SECONDS)}s — if Azure keeps returning "
            "429/5xx the script will abort with the real upstream error "
            "instead of retrying forever."
        ),
    )
    parser.add_argument(
        "--compact",
        action="store_true",
        help="Emit compact JSON to stdout instead of indented JSON.",
    )

    args = parser.parse_args(argv)
    if not 1 <= args.count <= 10:
        parser.error("--count must be between 1 and 10.")
    if args.max_attempts < 1:
        parser.error("--max-attempts must be at least 1.")
    if args.max_attempts > _HARD_MAX_ATTEMPTS:
        parser.error(
            f"--max-attempts may not exceed {_HARD_MAX_ATTEMPTS}. "
            f"Retrying more than that against an overloaded Azure endpoint "
            f"hides the real error instead of fixing anything. If you keep "
            f"hitting transient failures, investigate the Azure-side cause "
            f"(quota, region capacity, deployment SKU)."
        )
    if args.output_compression is not None and not 0 <= args.output_compression <= 100:
        parser.error("--output-compression must be between 0 and 100.")
    if args.edit_image and not Path(args.edit_image).is_file():
        parser.error(f"--edit-image not found: {args.edit_image}")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    config = resolve_config(args)
    size = resolve_size(args)
    output_dir = Path(args.output_dir).resolve()
    is_edit = bool(args.edit_image)
    operation = "edits" if is_edit else "generations"
    url = build_url(config, operation)

    body: dict[str, Any] = {
        "model": config["deployment"],
        "prompt": args.prompt,
        "size": size,
        "n": args.count,
        "quality": args.quality,
        "output_format": args.output_format,
    }
    if args.output_compression is not None:
        body["output_compression"] = args.output_compression
    if config["transparent"]:
        body["background"] = "transparent"

    if is_edit:
        body["input_fidelity"] = args.input_fidelity
        fields = {key: str(value) for key, value in body.items()}
        payload = http_post(
            url,
            config["api_key"],
            multipart=(fields, [("image[]", Path(args.edit_image))]),
            timeout=args.timeout,
            max_attempts=args.max_attempts,
        )
    else:
        payload = http_post(
            url,
            config["api_key"],
            json_body=body,
            timeout=args.timeout,
            max_attempts=args.max_attempts,
        )

    saved = save_images(payload, output_dir, args.output_format)
    sanitized = sanitize_response(payload)

    result = {
        "operation": operation,
        "deployment": config["deployment"],
        "url": url,
        "size": size,
        "saved_images": saved,
        "response": sanitized,
    }

    json.dump(result, sys.stdout, indent=None if args.compact else 2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
