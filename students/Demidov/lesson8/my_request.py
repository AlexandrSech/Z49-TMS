# import requests
import json

# Распаковка значений

# l = [1, 2, 3, 4]

# first, *_, last = l

# print(first, last)

class MyFirstPost:
    import requests

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def post_to_url(self, url):
        m1 = MyFirstPost(text='qwerty')
        return self.requests.post(url, json=self.__dict__).text

d = {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2021-05-28T17:02:17.818Z",
  "status": "placed",
  "complete": True,
}

m = MyFirstPost(**d)

r = m.post_to_url('https://petstore.swagger.io/v2/store/order')
print(r)

exit()

response = requests.post(url = 'https://petstore.swagger.io/v2/store/order', json = my_body)

print(response.text)

response = requests.get('https://petstore.swagger.io/v2/store/inventory')

text = response.text
print(text)

js = json.loads(text)
print(js)