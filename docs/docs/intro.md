---
slug: /
sidebar_position: 1
---

# Introduction

**example-lib** is a Python HTTP client library that provides a simple interface for making API requests.

## Features

- Simple, intuitive API for GET and POST requests
- Configurable request timeouts
- Automatic retry logic with exponential backoff for connection errors
- Response parsing utilities

## Quick Example

```python
from example_lib import Client

client = Client("https://api.example.com")
response = client.get("/users")
```

## Next Steps

- [Getting Started](./getting-started) — Installation and basic setup
- [API Reference](./api-reference) — Full class and method documentation
- [Utilities](./utilities) — Helper functions for working with responses
