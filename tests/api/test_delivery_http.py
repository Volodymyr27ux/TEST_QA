import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.delivery.com/')
    print(f"Response is {r.text}")
    assert r.status_code == 200
    headers = r.headers
    assert headers['Content-Type'] == 'text/html; charset=UTF-8' 
    assert headers['Cache-Control'] == 'no-cache'


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.delivery.com/merchant/search/delivery')
    body = r.json()
    headers = r.headers
    assert body['message'][0]['field'] == 'address'
    assert body['message'][1]['field'] == 'latitude'
    assert r.status_code == 400
    assert headers['Content-Type'] == 'application/json'
    assert headers['Vary'] == 'Accept-Encoding'


@pytest.mark.http
def test_id_request():
    r = requests.get('https://api.delivery.com/data/search/?%3Fsubsection=red.cabernet-sauvignon%3Ffilter_size%3D750mL,1L')
    assert r.status_code == 200


@pytest.mark.http
def test_product_request():
    r = requests.get('https://api.delivery.com/data/search/?search_type=alcohol')
    assert r.status_code == 200


@pytest.mark.http
def test_guest_token():
    url = 'https://api.delivery.com/data/customer/auth/guest'
    data_to_send = {"client_id": "NDY4NDAzYzViYmI0YWM0NTM3NTJmYzhmZWJkMWQwMWZi"}
    r = requests.get(url,json=data_to_send)
    assert r.status_code == 200 
    

@pytest.mark.http
def test_customer_cart():
    r = requests.get('https://api.delivery.com/data/customer/cart',json={"order_type": "pickup"})
    assert r.status_code == 200