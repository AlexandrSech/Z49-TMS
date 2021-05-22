people_num = int(input('Введите число гостей\n'))
if people_num > 50:
    print('ресторан')
elif people_num >= 20 and people_num <= 50:
    print('кафе')
elif people_num < 20:
    print('дом')

