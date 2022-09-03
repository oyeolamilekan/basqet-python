import requests
import json


class NetworkClient():

    def __init__(self, pubKey, secretKey):
        self.pubKey = pubKey
        self.secretKey = secretKey
        self.base_url = 'https://api.basqet.com/v1/'
        self.headers = {"Content-Type": "Application/json",
                        "Authorization": f"Bearer {self.pubKey}"}

    def format_response(self, response: requests.Response) -> dict:
        response.raise_for_status()
        return response.json()

    def get(self, url: str, headers=None) -> dict:
        return self.format_response(requests.get(f"{self.base_url}{url}", headers=headers or self.headers))

    def post(self, url: str, data: dict, headers=None) -> dict:
        return self.format_response(requests.post(f"{self.base_url}{url}", data=json.dumps(data), headers=headers or self.headers))
