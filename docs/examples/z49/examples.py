def create_polindrom(str):
    n = 0
    while str[n:] != str[n:][::-1]:
        n += 1
    return str + str[:n][::-1]

r = create_polindrom('mama')

print(r)

