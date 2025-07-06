import pytest
import requests

class Client:
    def __init__(self, host ="http://localhost:3000", headers=None):
        self.host = host
        self.headers = headers or {
            'accept': '*/*',
            'Content-Type': 'application/json'
        }

    def register_user(self, json):
        path = self.host + "/auth/register"
        response = requests.request("POST", path, headers=self.headers, json=json)
        log = f"""
        REQUEST: 
            URL: {response.request.url}
            METHOD: {response.request.method}
            DATA: {response.request.body}

        RESPONSE:
            STATUS_CODE: {response.status_code}
            CONTENT: {response.json()}
        """
        print(log)
        return response

    def login_user(self, json):
        path = self.host + "/auth/login"
        response = requests.request("POST", path, headers=self.headers, json=json)
        log = f"""
        REQUEST: 
            URL: {response.request.url}
            METHOD: {response.request.method}
            DATA: {response.request.body}
        
        RESPONSE:
            STATUS_CODE: {response.status_code}
            CONTENT: {response.json()}
        """
        print(log)
        return response

    def name_edit_user(self, json):
        path = self.host + "/user/name"
        response = requests.request("PATCH", path, headers=self.headers, json=json)
        log = f"""
        REQUEST: 
            URL: {response.request.url}
            METHOD: {response.request.method}
            DATA: {response.request.body}

            RESPONSE:
            STATUS_CODE: {response.status_code}
            CONTENT: {response.json()}
        """
        print(log)
        return response

    def exist_user(self, json):
        path = self.host + "/exist"
        response = requests.request("POST", path, headers=self.headers, json=json)
        log = f"""
        REQUEST: 
            URL: {response.request.url}
            METHOD: {response.request.method}
            DATA: {response.request.body}

        RESPONSE:
            STATUS_CODE: {response.status_code}
            CONTENT: {response.json()}
        """
        print(log)
        return response

    def update_headers(self, new_headers):
        self.headers.update(new_headers)


@pytest.fixture
def client():
  return Client()