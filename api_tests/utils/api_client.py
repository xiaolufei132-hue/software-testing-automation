"""封装 HTTP 请求客户端"""

import requests


class APIClient:
    """通用 API 请求封装"""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, endpoint: str, params: dict = None, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.get(url, params=params, **kwargs)

    def post(self, endpoint: str, json: dict = None, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.post(url, json=json, **kwargs)

    def put(self, endpoint: str, json: dict = None, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.put(url, json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.delete(url, **kwargs)

    def set_token(self, token: str):
        self.session.headers.update({"Authorization": f"Bearer {token}"})
