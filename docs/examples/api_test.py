
class MyList:
    rows: list
    text: str

    def __init__(self, data: dict):
        self.rows = []
        for k, v in data.items():
            if k == 'rows':
                self.rows.append(v)
            elif k == 'text':
                self.text = v


class API:
    import requests
    import json

    def __init__(self, url, user_name, password):
        self.url = url
        self.my_session = self.requests.session()
        response = self.my_session.get(self.url + 'get_token')
        self.token = self.json.loads(response.text)

    def __get(self, end_point):
        return self.json.loads(self.my_session.get(self.url + end_point).text)

    def get_list(self):
        self.current_list = MyList(self.__get('get_list'))


if __name__ == '__main__':
    api = API('http://127.0.0.1:8000/', '', '')
    print(api.token)
    api.get_list()
    print(api.current_list)
    print(api.current_list.text)
    for i in api.current_list.rows:
        print(i)

    # r = api.my_session.get(api.url + 'get_list')
    # print(r.text)
