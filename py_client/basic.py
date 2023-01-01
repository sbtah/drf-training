import requests


endpoint_app = "http://localhost:8000/api/"


response = requests.post(
    endpoint_app, json={"title": "Abc123..1", "content": "Hello", "price": 123.33}
)
print(response.json())
