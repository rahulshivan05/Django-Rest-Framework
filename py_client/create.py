import requests

headers = {'Authorization': 'Bearer 99363d16a3e0bdb0f4e8d7957d09aba3d3c27b90'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is done",
    "content": "lol content",
    "price": 32.99,
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
