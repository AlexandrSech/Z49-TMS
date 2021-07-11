import requests


def main(name, id):
    s = requests.session()
    r = s.post('http://127.0.0.1:50550/login', json={'login': name, 'id': id})
    print(r.text)
    r = s.get('http://127.0.0.1:50550/bip')
    print(r)
    r = s.get('http://127.0.0.1:50550/bip')
    print(r)
    r = s.get('http://127.0.0.1:50550/logout')
    print(r.text)


if __name__ == '__main__':
    main(
        input('name = '),
        input('id = ')
    )

