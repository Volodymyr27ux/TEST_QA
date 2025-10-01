import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user.get('login') == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r.get('total_count') == 57
    assert 'become-qa-auto' in r.get('items') [0] ['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r.get('total_count') == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r.get('total_count') != 0


@pytest.mark.api
def test_emojis(github_api):
    r = github_api.get_emojis()
    assert r['abc'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f524.png?v8'
    assert r['apple'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f34e.png?v8'


@pytest.mark.api
def test_commits(github_api):
    r = github_api.list_commits('Volodymyr27ux','TEST_QA')    
    assert r[0]['commit']['author']['name'] == 'Volodymyr Chernenko'
    assert r[1]['author']['login'] == 'Volodymyr27ux'


@pytest.mark.api
def test_not_found_commits(github_api):
    r = github_api.list_commits('Volodymyr27','TEST_QA')
    assert r['message'] == 'Not Found'
