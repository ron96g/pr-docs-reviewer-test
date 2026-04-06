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
- **`max_retries`** (`int`, default=`3`): Maximum number of retry attempts for requests that encounter connection errors.
- **`backoff_factor`** (`float`, default=`0.5`): Multiplier for exponential backoff between retry attempts. The sleep time before the Nth retry is `backoff_factor * (2 ** (N-1))` seconds.
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

The client raises standard exceptions for common failure modes. With the new retry mechanism, `ConnectionError`s will trigger retries. If all retry attempts are exhausted, a `RetryError` will be raised. `TimeoutError`s are not retried.

```python
from example_lib import Client
from example_lib.exceptions import TimeoutError, RetryError # Import RetryError

client = Client("https://api.example.com", max_retries=2) # Example with retries

try:
    response = client.get("/flakey-endpoint")
    # For a direct timeout (not retried)
    response_slow = client.get("/slow-endpoint")
except TimeoutError:
    print("Request timed out after configured timeout.")
except RetryError as e: # Catch RetryError for persistent connection issues
    print(f"Request failed after multiple retries: {e}")
    # You can access the last underlying error via e.__cause__ if needed
```
