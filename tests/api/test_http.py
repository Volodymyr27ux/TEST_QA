import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body.get('name') == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server'] == 'github.com'

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 404

@pytest.mark.http
def test_status_code_emojis():
    r = requests.get('https://api.github.com/emojis')

    assert r.status_code == 200

@pytest.mark.http
def test_commits():
    r = requests.get('https://api.github.com/repos/Volodymyr27ux/TEST_QA/commits')
    
    assert r.status_code == 200
    
