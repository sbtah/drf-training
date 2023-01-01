import requests


# endpoint_app = f"http://localhost:8000/api/products/{}"
response = requests.delete("http://localhost:8000/api/products/5/delete/")
print(response.status_code, response.status_code == 204)
