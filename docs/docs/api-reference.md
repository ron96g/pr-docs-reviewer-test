---
sidebar_position: 3
---

# API Reference

## Client

The main class for interacting with HTTP APIs.

### `Client(base_url, timeout=30, max_retries=3, backoff_factor=0.5)`

Creates a new API client instance with optional retry logic for network errors.

**Parameters:**

| Parameter        | Type    | Default | Description                                                                                                                                                                                                 |
|------------------|---------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `base_url`       | `str`   | —       | The base URL for all API requests                                                                                                                                                                           |
| `timeout`        | `int`   | `30`    | Request timeout in seconds                                                                                                                                                                                  |
| `max_retries`    | `int`   | `3`     | The total number of attempts to make for a request, including the initial request. Defaults to 3 (1 initial attempt + 2 retries). If all attempts fail due to a retryable error, a `RetryError` is raised. |
| `backoff_factor` | `float` | `0.5`   | A floating-point multiplier used in the exponential backoff calculation. The delay between retries is calculated as `backoff_factor * (2 ** attempt_number)`, where `attempt_number` starts from 0 for the first retry. |

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

### `RetryError`

Raised when all configured retry attempts for a network request have been exhausted due to a retryable connection error.
