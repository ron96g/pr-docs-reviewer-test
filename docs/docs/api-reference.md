---
sidebar_position: 3
---

# API Reference

## Client

The main class for interacting with HTTP APIs.

### `Client(base_url, timeout=30, max_retries=3, backoff_factor=0.5)`

Creates a new API client instance.

**Parameters:**

| Parameter        | Type    | Default | Description                                            |
|------------------|---------|---------|--------------------------------------------------------|
| `base_url`       | `str`   | —       | The base URL for all API requests                      |
| `timeout`        | `int`   | `30`    | Request timeout in seconds                             |
| `max_retries`    | `int`   | `3`     | Maximum number of retry attempts for failed requests.  |
| `backoff_factor` | `float` | `0.5`   | Multiplier for exponential backoff between retries.    |

**Example:**

```python
from example_lib import Client

client = Client("https://api.example.com", timeout=60, max_retries=5, backoff_factor=1.0)
```

---

### `Client.get(path)`

Sends a GET request to the specified path, appended to the client's `base_url`.

**Parameters:**

| Parameter | Type  | Description                      |
|-----------|-------|----------------------------------|
| `path`    | `str` | The API endpoint path (e.g. `/users`) |

**Returns:** `Response` object

**Example:**

```python
response = client.get("/users")
```

---

### `Client.post(path, data)`

Sends a POST request with a JSON body.

**Parameters:**

| Parameter | Type   | Description                          |
|-----------|--------|--------------------------------------|
| `path`    | `str`  | The API endpoint path                |
| `data`    | `dict` | The request body, serialized as JSON |

**Returns:** `Response` object

**Example:**

```python
response = client.post("/users", data={"name": "Alice"})
```

---

## Exceptions

### `TimeoutError`

Raised when a request exceeds the configured `timeout` duration.

### `ConnectionError`

Raised when the client cannot establish a connection to the server. Note that `ConnectionError`s are now subject to the client's retry mechanism; if all retries are exhausted, a `RetryError` will be raised instead.

### `RetryError`

Raised when all retry attempts for a request have been exhausted due to underlying connection errors. This indicates that the client was unable to successfully complete the request after multiple retries.