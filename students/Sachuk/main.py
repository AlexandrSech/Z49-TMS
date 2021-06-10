import requests
import json



my_url = 'https://stepik.org/explore'
response = requests.get(my_url)
print(response.headers)



exit()

response = requests.get('https://petstore.swagger.io/v2/store/inventory')
print(response.status_code)


class MyFirstPost:
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def post_to_url(self, url):
        m1 = MyFirstPost(text='qwerty')
        return requests.post(url, json=self.__dict__).text


d = {
    "id": 0,
    "petId": 0,
    "quantity": 0,
    "shipDate": "2021-05-28T18:21:57.502Z",
    "status": "placed",
    "complete": True
}

first_post = MyFirstPost(**d)
r = first_post.post_to_url(url='https://petstore.swagger.io/v2/store/order')
print(r)

response_from_post = requests.post(url='https://petstore.swagger.io/v2/store/order', json=d)
print(response_from_post.status_code)
print(response_from_post.text)
