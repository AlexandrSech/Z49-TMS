'''Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия.
Вывести все сведения о поездах,
время пребывания в пути которых превышает 7 часов 20 минут'''
import datetime
slov = {999: ["Москва", 2021, 5, 12, 19, 30, 0 , 'Уфа', 2021, 5, 13, 7, 00, 00]}
time = 0

for i in slov:
    a = datetime.datetime(slov[i][1], slov[i][2], slov[i][3], slov[i][4], slov[i][5])
    b = datetime.datetime(slov[i][-6], slov[i][-5], slov[i][-4], slov[i][-3], slov[i][-2])
    iz = a.strftime("%Y.%m.%d %H:%M")
    to = b.strftime("%Y.%m.%d %H:%M")
    time = abs(a - b)
    if time.seconds > 26400:
        print("Поезд отправляется из", slov[i][0], iz, 'и прибывает в', slov[i][-7], to)

