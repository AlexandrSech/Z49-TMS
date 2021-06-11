def palindrom(strin):
    if strin[::-1] == strin:
        return 'ДА'
    else:
        return 'НЕТ'

strin = str(input('Введите слово: '))
print(palindrom(strin))