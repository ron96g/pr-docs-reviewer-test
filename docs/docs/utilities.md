---
sidebar_position: 4
---

# Utilities

Helper functions for working with API responses.

## `parse_response(response)`

Parses a raw API response into a structured result dictionary.

**Parameters:**

| Parameter  | Type       | Description                 |
|------------|------------|-----------------------------|
| `response` | `Response` | The response object to parse |

**Returns:** `dict` with the following keys:

| Key        | Type   | Description                            |
|------------|--------|----------------------------------------|
| `status`   | `str`  | `"ok"` or `"error"`                    |
| `data`     | `dict` | The parsed response body               |
| `headers`  | `dict` | Response headers as a plain dictionary |

**Example:**

```python
from example_lib.utils import parse_response

response = client.get("/users")
result = parse_response(response)

if result["status"] == "ok":
    users = result["data"]
```

## `build_url(base, path, params=None)`

Constructs a full URL from a base URL, path, and optional query parameters.

**Parameters:**

| Parameter | Type             | Default | Description              |
|-----------|------------------|---------|--------------------------|
| `base`    | `str`            | —       | The base URL             |
| `path`    | `str`            | —       | The endpoint path        |
| `params`  | `dict` or `None` | `None`  | Query parameters to append |

**Returns:** `str` — the fully constructed URL

**Example:**

```python
from example_lib.utils import build_url

url = build_url("https://api.example.com", "/search", params={"q": "python"})
# => "https://api.example.com/search?q=python"
```
