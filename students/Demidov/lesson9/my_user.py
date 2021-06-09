import requests
from requests.sessions import session


class Muser():
    import requests
    nickname: str
    url: str

    def get_url(self):
        self.r = self.requests.get(self.url)
        return  self.r.status_code

    def __init__(self, nickname, url):
        self.my_session = self.requests.session()
        self.nickname = nickname
        self.url = url
        response = self.my_session.get(self.url)
        print(response.status_code)