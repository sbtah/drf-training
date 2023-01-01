import requests


endpoint = "http://localhost:8000/api/products/create/"
data = {
    "title": "Mega Product!",
}

response = requests.post(
    endpoint,
    json=data,
)
print(response.json())
