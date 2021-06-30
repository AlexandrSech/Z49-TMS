'''Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
год. Найти самую раннюю дату.'''

import csv
import random

dates = [
    [random.randint(1, 30), random.randint(0, 12), random.randint(1999, 2021)],
    [random.randint(1, 30), random.randint(0, 12), random.randint(1999, 2021)],
    [random.randint(1, 30), random.randint(0, 12), random.randint(1999, 2021)],
    [random.randint(1, 30), random.randint(0, 12), random.randint(1999, 2021)],
    [random.randint(1, 30), random.randint(0, 12), random.randint(1999, 2021)],
    [random.randint(1, 30), random.randint(0, 12), random.randint(1999, 2021)],
    [random.randint(1, 30), random.randint(0, 12), random.randint(1999, 2021)],
]
yer = mont = day = 10000
a = b = 0
with open('date.csv', 'w+') as f:
    writer = csv.writer(f)
    writer.writerows(dates)
    f.seek(0)
    reader = csv.reader(f)
    m = list(reader)
    for i in m:
        i[0], i[1], i[2] = int(i[0]), int(i[1]), int(i[2])
        if i[2] < yer:
            yer = i[2]
            a = b
        elif i[2] == yer:
            if i[1] < mont:
                mont = i[1]
                a = b
            elif i[1] == mont:
                if i[0] < day:
                    day = i[0]
                    a = b
        b += 1
    print(m[a])