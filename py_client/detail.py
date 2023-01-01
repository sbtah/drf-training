import requests


# endpoint_app = f"http://localhost:8000/api/products/{}"

response = requests.get("http://localhost:8000/api/products/4/")
print(response.json())
