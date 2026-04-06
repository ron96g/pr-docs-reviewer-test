---
sidebar_position: 2
---

# Getting Started

## Installation

Install example-lib via pip:

```bash
pip install example-lib
```

## Configuration

Create a `Client` instance with your API base URL:

```python
from example_lib import Client

client = Client("https://api.example.com")
```

The `Client` constructor accepts the following parameters:

- **`base_url`** (`str`): The base URL for all API requests. Must include the scheme (`https://`).
- **`timeout`** (`int`, default=`30`): Request timeout in seconds. Requests that exceed this duration will raise a `TimeoutError`.

## Basic Usage

### Making GET requests

```python
response = client.get("/users")
print(response.status_code)
print(response.json())
```

### Making POST requests

```python
data = {"name": "Alice", "email": "alice@example.com"}
response = client.post("/users", data=data)
```

## Error Handling

The client raises standard exceptions for common failure modes:

```python
from example_lib.exceptions import TimeoutError, ConnectionError

try:
    response = client.get("/slow-endpoint")
except TimeoutError:
    print("Request timed out")
except ConnectionError:
    print("Could not connect to server")
```
