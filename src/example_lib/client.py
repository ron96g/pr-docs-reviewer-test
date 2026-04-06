"""HTTP client for example-lib."""

import time
import urllib.request
import json


class TimeoutError(Exception):
    """Raised when a request exceeds the configured timeout."""
    pass


class ConnectionError(Exception):
    """Raised when a connection cannot be established."""
    pass


class RetryError(Exception):
    """Raised when all retry attempts have been exhausted."""
    pass


class Response:
    """Simple response wrapper."""

    def __init__(self, status_code: int, body: bytes, headers: dict):
        self.status_code = status_code
        self.body = body
        self.headers = headers

    def json(self) -> dict:
        return json.loads(self.body)

    def text(self) -> str:
        return self.body.decode("utf-8")


class Client:
    """An HTTP client for making API requests.

    Args:
        base_url: The base URL for all API requests.
        timeout: Request timeout in seconds.
        max_retries: Maximum number of retry attempts for failed requests.
        backoff_factor: Multiplier for exponential backoff between retries.
    """

    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
        max_retries: int = 3,
        backoff_factor: float = 0.5,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def _request(self, method: str, path: str, body: bytes | None = None, headers: dict | None = None) -> Response:
        """Send an HTTP request with retry logic.

        Retries on connection errors using exponential backoff. Timeout errors
        are not retried.

        Args:
            method: The HTTP method (GET, POST, etc.).
            path: The API endpoint path.
            body: Optional request body bytes.
            headers: Optional request headers.

        Returns:
            A Response object.

        Raises:
            TimeoutError: If the request times out.
            RetryError: If all retry attempts are exhausted.
        """
        url = f"{self.base_url}{path}"
        last_error = None

        for attempt in range(self.max_retries):
            try:
                req = urllib.request.Request(url, data=body, method=method, headers=headers or {})
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    return Response(
                        status_code=resp.status,
                        body=resp.read(),
                        headers=dict(resp.headers),
                    )
            except urllib.error.URLError as e:
                if "timed out" in str(e):
                    raise TimeoutError(f"Request to {url} timed out") from e
                last_error = e
                if attempt < self.max_retries - 1:
                    sleep_time = self.backoff_factor * (2 ** attempt)
                    time.sleep(sleep_time)

        raise RetryError(
            f"Request to {url} failed after {self.max_retries} attempts"
        ) from last_error

    def get(self, path: str) -> Response:
        """Send a GET request.

        Args:
            path: The API endpoint path.

        Returns:
            A Response object.
        """
        return self._request("GET", path)

    def post(self, path: str, data: dict) -> Response:
        """Send a POST request with a JSON body.

        Args:
            path: The API endpoint path.
            data: The request body, serialized as JSON.

        Returns:
            A Response object.
        """
        body = json.dumps(data).encode("utf-8")
        return self._request("POST", path, body=body, headers={"Content-Type": "application/json"})
