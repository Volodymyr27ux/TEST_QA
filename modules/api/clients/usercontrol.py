import requests


class Usercontrol:

    def user_login(self,data_user):
        r = requests.post('https://conduit-api.learnwebdriverio.com/api/users/login', json=data_user)
        body = r.json()
        return body