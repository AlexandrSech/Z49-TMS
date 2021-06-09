# Создать строку равную первым пяти символам введенной строки.

s = input()

if len(s) > 4:
    result = s[0:5:]
    print(result)
else:
    print('Length of a word is less then 5')