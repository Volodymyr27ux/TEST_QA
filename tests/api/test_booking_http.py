import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://supply-xml.booking.com/rooms-api/meta')
    body = r.json()
    assert r.status_code == 200
    assert body['data']['unit_types'][0]['suggested_unit_names'][0]['unit_name']== 'Apartment'
    assert body['data']['unit_types'][0]['suggested_unit_names'][1]['unit_name']== 'Apartment with Balcony'