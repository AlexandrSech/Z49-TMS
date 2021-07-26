import pal


def test_get_pal():
    r = pal.get_pal('aaba') == 'aabaa'
    print(r if r else 'Error')


def test_get_pal2():
    assert pal.get_pal('aaba') == 'aabaa', 'Some error'


if __name__ == '__main__':
    test_get_pal2()
