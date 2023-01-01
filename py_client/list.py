import requests
from get_token import get_token


token = get_token()


if token:
    headers = {
        "Authorization": f"Bearer {token}",
    }
    endpoint = "http://localhost:8000/api/products/"
    response = requests.get(endpoint, headers=headers)
    print(response.json())
