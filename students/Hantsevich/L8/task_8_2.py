def is_polyndrome(word: str):
    if word == word[::-1]:
        print(word, ">>> is polyndrome")
    else:
        print(word, '>>> is not polyndrome')

word = str(input('ВВедите слово:'))
print(is_polyndrome(word))

