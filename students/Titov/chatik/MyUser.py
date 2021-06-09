import json


class MUser:
    import requests
    import json
    nickname: str
    url_connect: str

    def get_url(self):
        self.r = self.requests.get(self.url_connect)
        return self.r.status_code

    def __init__(self, nickname, url):
        self.my_session = self.requests.session()
        self.nickname = nickname
        self.url_connect = url
        response = self.my_session.get(self.url_connect)
        print(response.status_code)

    def post_login(self):
        response = self.my_session.post(url=self.url_connect + '/login', json={'u_name': self.nickname})
        return f'{response.status_code} {response.text}'

    def post_logout(self):
        response = self.my_session.post(url=self.url_connect + '/logout', json={'u_name': self.nickname})
        return f'{response.status_code} {response.text}'

    def get_messages(self):
        response = self.my_session.get(url=self.url_connect + '/get_messages')
        #print(response.text)
        return self.json.loads(response.text)['rows']

    def send_messages(self, text):
        import time
        response = self.my_session.post(url=self.url_connect + '/send_message',
                                        json={"message_text": text, "time": time.time(), "u_name": self.nickname})
        return response.text


