import requests

# endpoint = "https://httpbin.org/anything"
# endpoint = "http://localhost:8000/api/"  # https://localhost:8000/
endpoint = "http://localhost:8000/api/create/"  # https://localhost:8000/

# API --> Application programming interface

# ---------------------- Get the data from the DB
# get_response = requests.get(endpoint, json={
#     "title": 'Hello World'})

# ---------------------- Post the data into the DB
get_response = requests.post(endpoint, json={
    "title": "Abc123",
    "content": 'Hello World',
    "price": "123A"
})

# Phone -> Camera uses by the App -> by using API -> of camera.

# print(get_response.text)  # prints the source code/ raw text response

# HTTP Request --> HTML
# REST API HTTP Request --> JSON(xml)
# JavaScript Object Notation(JSON) ~ Python Dictonary.

# print(get_response.text)

print(get_response.json())  # only return the JSON data
# print(get_response.headers)
# print(get_response.text)
