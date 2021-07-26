
def palindrom1(_str):
    if not _str:
        return None
    return _str + _str[:-1][::-1]


passed = True
assert palindrom1('mama') == 'mamam', 'Not passed'


if __name__ == '__main__':
    print(palindrom1('mama'))
