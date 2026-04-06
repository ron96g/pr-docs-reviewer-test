---
sidebar_position: 3
---

# API Reference

## Client

The main class for interacting with HTTP APIs.

### `Client(base_url, timeout=30)`

Creates a new API client instance.

**Parameters:**

| Parameter  | Type  | Default | Description                                  |
|------------|-------|---------|----------------------------------------------|
| `base_url` | `str` | —       | The base URL for all API requests             |
| `timeout`  | `int` | `30`    | Request timeout in seconds                    |

**Example:**

```python
from example_lib import Client

client = Client("https://api.example.com", timeout=60)
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

Raised when the client cannot establish a connection to the server.
