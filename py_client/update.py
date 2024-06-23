import requests

endpoint = "http://localhost:8000/api/products/9/update/"

data = {
    "title": "Hello world my old friends",
    "price": 129.99
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
