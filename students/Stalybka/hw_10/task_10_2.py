"""
Создать csv файл с данными о ежедневной погоде. Структура: Дата,
Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
градусы) для Минск за последние 7 дней.
"""

import csv
import datetime

data = [
    ['Дата','Место', 'Градусы', 'Скорость ветра'],
    [datetime.date(2021, 6, 13), 'Minsk', 17, 13.0],
    [datetime.date(2021, 6, 14), 'Minsk', 20, 14.5],
    [datetime.date(2021, 6, 15), 'Minsk', 23, 11.1],
    [datetime.date(2021, 6, 16), 'Minsk', 22, 13.0],
    [datetime.date(2021, 6, 17), 'Minsk', 24, 9.3],
    [datetime.date(2021, 6, 18), 'Minsk', 26, 11.1],
    [datetime.date(2021, 6, 19), 'Minsk', 28, 10],
]
'''
with open('weather.cvs', 'w') as f:
    file_writer = csv.writer(f, delimiter=',')
    file_writer.writerows(data)
  '''
with open('weather.cvs', 'r') as f:
    file_reader = csv.reader(f)
    aver_tem = 0
    aver_wind = 0

    for row in file_reader:
        if row[0] == 'Дата':
            pass
        else:
            aver_tem += int(row[2])
            aver_wind += float(row[3])

    aver_tem /= int(len(data)) - 1
    aver_wind /= int(len(data)) - 1

    print(f'Средняя скорость ветра = {aver_wind:.2f}'
          f'\nСредняя температура = {aver_tem:.1f}')

