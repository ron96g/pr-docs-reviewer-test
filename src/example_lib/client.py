"""HTTP client for example-lib."""

import urllib.request
import json


class TimeoutError(Exception):
    """Raised when a request exceeds the configured timeout."""
    pass


class ConnectionError(Exception):
    """Raised when a connection cannot be established."""
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
    """

    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, path: str) -> Response:
        """Send a GET request.

        Args:
            path: The API endpoint path.

        Returns:
            A Response object.
        """
        url = f"{self.base_url}{path}"
        try:
            req = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return Response(
                    status_code=resp.status,
                    body=resp.read(),
                    headers=dict(resp.headers),
                )
        except urllib.error.URLError as e:
            if "timed out" in str(e):
                raise TimeoutError(f"Request to {url} timed out") from e
            raise ConnectionError(f"Could not connect to {url}") from e

    def post(self, path: str, data: dict) -> Response:
        """Send a POST request with a JSON body.

        Args:
            path: The API endpoint path.
            data: The request body, serialized as JSON.

        Returns:
            A Response object.
        """
        url = f"{self.base_url}{path}"
        body = json.dumps(data).encode("utf-8")
        try:
            req = urllib.request.Request(
                url,
                data=body,
                method="POST",
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return Response(
                    status_code=resp.status,
                    body=resp.read(),
                    headers=dict(resp.headers),
                )
        except urllib.error.URLError as e:
            if "timed out" in str(e):
                raise TimeoutError(f"Request to {url} timed out") from e
            raise ConnectionError(f"Could not connect to {url}") from e
