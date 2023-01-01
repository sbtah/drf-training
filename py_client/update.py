import requests


# endpoint_app = f"http://localhost:8000/api/products/{}"
data = {
    "title": "This title was updated",
    "price": 999.99,
}
response = requests.put("http://localhost:8000/api/products/5/update/", json=data)
print(response.json())
