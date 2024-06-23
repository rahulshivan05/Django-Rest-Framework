
# Django Rest Framework

In this project we make a small framework for our web for Testing how the rest framework is working in the Backen


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


# Hi, I'm Rahul Kumar Gupta! 👋


## Environment Variables

To run this project, you will need to activate the following environment variables to your project

`Python -m venv venv`

`cd venv`

for mac user
`source/bin/activate`

for Windows user
`cd Scripts` and then type `activate`






## Installation

Install my-project with python or fork it and also clone it.

After `Activiting` the Virtual environment then install the packages using

```bash
  pip install -r requirements.txt
```
    
## API Reference

#### Get all items

```http
  GET /api/products/
```
But you have to Login in Django

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Doesn't require any api key**  |

#### Get item by using ID
for Update or Delete the Products from the Database

```http
  GET /api/products/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


## Documentation

[Django](https://www.djangoproject.com/)


[Django Rest Framework](https://www.django-rest-framework.org/)


## Authors

- [Rahul Kumar Gupta](https://www.github.com/rahulshivan05)

