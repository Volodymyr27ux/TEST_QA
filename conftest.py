import pytest
import requests
from modules.api.clients.github import GitHub
from modules.api.clients.usercontrol import Usercontrol


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Volodymyr"
        self.second_name = "Chernenko"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def hello():
    print('Hello this is fixture')
    yield 'my name is Volodymyr'

    print('End of the test')


@pytest.fixture
def usercontrol_api():
    user = Usercontrol()
    
    yield user


@pytest.fixture
def session():
    http_session = requests.Session()

    yield http_session

    http_session.close()


@pytest.fixture
def next_session():
    http_session = requests.Session()
    data_user = {'user':{'email': 'test@bg.com','password': '12345'}}
    r = http_session.post('https://conduit-api.learnwebdriverio.com/api/users/login', json=data_user)
    token = r.json()['user']['token']
    http_session.headers.update({'Authorization': f'Token {token}'})

    yield http_session

    http_session.close()