"""Utility functions for working with API responses."""

from urllib.parse import urlencode


def parse_response(response) -> dict:
    """Parse a raw API response into a structured result.

    Args:
        response: The Response object to parse.

    Returns:
        A dict with keys: status, data, headers.
    """
    try:
        data = response.json()
        status = "ok" if response.status_code < 400 else "error"
    except Exception:
        data = {}
        status = "error"

    return {
        "status": status,
        "data": data,
        "headers": dict(response.headers) if hasattr(response, "headers") else {},
    }


def build_url(base: str, path: str, params: dict | None = None) -> str:
    """Construct a full URL from base, path, and optional query parameters.

    Args:
        base: The base URL.
        path: The endpoint path.
        params: Optional query parameters to append.

    Returns:
        The fully constructed URL string.
    """
    url = f"{base.rstrip('/')}{path}"
    if params:
        url = f"{url}?{urlencode(params)}"
    return url
