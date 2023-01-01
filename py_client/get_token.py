import requests
from getpass import getpass


def get_token():
    auth_endpoint = "http://localhost:8000/api/auth/"
    password = getpass()

    auth_response = requests.post(
        auth_endpoint, json={"username": "Sbtha", "password": password}
    )
    token = auth_response.json().get("token")
    return token
