import pytest
import requests


@pytest.mark.http
def test_create_pet():
    url = 'https://petstore.swagger.io/v2/pet'
    data_to_send = {
        "id": 0,
        "category": {
        "id": 0,
        "name": "cat"
    },
        "name": "pussy",
        "photoUrls": [
        "string"
    ],
        "tags": [
    {
      "id": 0,
      "name": "string"
    }
    ],
      "status": "available"
    }
    r = requests.post(url,json=data_to_send)
    body = r.json()
    print(body)
    assert r.status_code == 200


@pytest.mark.http
def test_check_pet_by_id():
    r = requests.get('https://petstore.swagger.io/v2/pet/9223372036854775807')
    assert r.status_code == 200


@pytest.mark.http
def test_create_order():
    url ='https://petstore.swagger.io/v2/store/order'
    data_to_send = {
  "id": 0,
  "petId": 9223372036854775807,
  "quantity": 45,
  "shipDate": "",
  "status": "placed",
  "complete": True
  }
    r = requests.post(url,json=data_to_send)
    assert r.status_code == 200
    body = r.json()
    print(body)


@pytest.mark.http
def test_check_order_by_id():
    r = requests.get('https://petstore.swagger.io/v2/store/order/9222968140497182329')
    assert r.status_code == 200
    body = r.json()
    print(body)


@pytest.mark.http
def test_create_user():
    url = 'https://petstore.swagger.io/v2/user'
    data_to_send = [
  {
    "id": 0,
    "username": "Tarik07",
    "firstName": "TARAS",
    "lastName": "TARASOV",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }
  ]
    r = requests.post(url,json=data_to_send)
    assert r.status_code == 200


@pytest.mark.http
def test_check_created_user():
    r = requests.get('https://petstore.swagger.io/v2/user/Tarik07')
    body = r.json()
    print(body)
    assert r.status_code == 200


@pytest.mark.http
def test_update_username():
    url = 'https://petstore.swagger.io/v2/user/Tarik07'
    data_to_send = [
  {
    "id": 0,
    "username": "Tarrow",
    "firstName": "TARAS",
    "lastName": "TARASOV",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }
  ]
    r = requests.put(url,json=data_to_send)
    assert r.status_code == 500
    body = r.json()