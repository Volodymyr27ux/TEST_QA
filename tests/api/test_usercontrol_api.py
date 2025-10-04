import pytest


@pytest.mark.api
def test_check_login(usercontrol_api):
    r = usercontrol_api.user_login({'user':{'email': 'test@bg.com','password': '12345'}})
    key_list = r['user'].keys()
    assert 'username' in key_list
    assert 'email' in key_list
    assert 'token' in key_list
    

@pytest.mark.api
def test_invalid_login(usercontrol_api):
    r = usercontrol_api.user_login({'user':{'email': 'test@http.com','password': '1234'}})
    assert r['errors'] == {'email or password': 'is invalid'}


@pytest.mark.api
def test_create_article(next_session):
    data_user = {'article':{'author':{},'title':'test','description':'QA Auto','body':'QA Automation trainee','tagList':[]}}
    r = next_session.post('https://conduit-api.learnwebdriverio.com/api/articles', json=data_user)
    body = r.json()
    assert r.ok
    assert body['article']['body'] == 'QA Automation trainee'
    assert body['article']['description'] == 'QA Auto'


@pytest.mark.api
def test_post_comment(next_session):
    data = {'comment':{'body':'Hello everybody'}}
    r = next_session.post('https://conduit-api.learnwebdriverio.com/api/articles/test-muhh58/comments',json=data)
    body = r.json()
    assert r.ok
    assert body['comment']['body'] == 'Hello everybody'
    print(body)