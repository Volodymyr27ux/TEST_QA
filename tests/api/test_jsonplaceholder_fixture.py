import pytest


@pytest.mark.http
def test_first_request(session):
    r = session.get('https://jsonplaceholder.typicode.com/posts/1')
    body = r.json()
    assert r.status_code == 200
    assert body['id'] == 1
    headers = r.headers
    assert headers['vary'] == 'Origin, Accept-Encoding'
    assert headers['Server'] == 'cloudflare'


@pytest.mark.http
def test_second_request(session):
    r = session.get('https://jsonplaceholder.typicode.com/comments?postId=1')
    body = r.json()
    assert r.ok
    assert body[2]['name'] == 'odio adipisci rerum aut animi'
    assert body[3]['name'] == 'alias odio sit'
    

@pytest.mark.http
def test_put_request(session,hello):
    body = {
         'id' : 1,
         'title': 'foo',
         'Body': 'bar',
         'userId': 127,
         'name' : 'Volodymyr'
    }
    headers =  {'Content-type': 'application/json; charset=UTF-8'}
    r = session.put('https://jsonplaceholder.typicode.com/posts/1', json=body, headers=headers)
    assert r.status_code == 200
    assert r.json()['userId'] == 127
    assert r.json()['name'] == 'Volodymyr'
    assert r.json() == body
    assert 'Volodymyr' in hello

