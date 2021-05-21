str_4 = input('Введите строку\n')
if len(str_4) % 2 !=0:
    middle_letter = str_4[len(str_4) // 2]
    print(middle_letter)
if middle_letter == str_4[0]:
    print(str_4[1:-1])
else:
    print('В строке четное кол-во символов, у него нет средней буквы')

