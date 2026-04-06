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

client = Client("https://api.example.com", max_retries=5, backoff_factor=1.0)
```

The `Client` constructor accepts the following parameters:

- **`base_url`** (`str`): The base URL for all API requests. Must include the scheme (`https://`).
- **`timeout`** (`int`, default=`30`): Request timeout in seconds. Requests that exceed this duration will raise a `TimeoutError`.
- **`max_retries`** (`int`, default=`3`): The total number of attempts to make for a request, including the initial request. Defaults to 3 (1 initial attempt + 2 retries). If all attempts fail due to a retryable error, a `RetryError` is raised.
- **`backoff_factor`** (`float`, default=`0.5`): A floating-point multiplier used in the exponential backoff calculation. The delay between retries is calculated as `backoff_factor * (2 ** attempt_number)`, where `attempt_number` starts from 0 for the first retry.

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

The client raises specific exceptions for common failure modes, including network issues and timeouts. The `Client` now includes retry logic, so direct `ConnectionError` exceptions are replaced by `RetryError` if all retry attempts are exhausted, or `TimeoutError` if the initial or any retry attempt times out.

```python
from example_lib.client import TimeoutError, RetryError

try:
    response = client.get("/flaky-endpoint")
except TimeoutError:
    print("Request timed out")
except RetryError:
    print("Could not connect to server after multiple retries")
```
