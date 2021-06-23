"""
Дан файл, содержащий различные даты. Каждая дата - это число, месяц игод. Найти самую раннюю дату
"""
import csv
import datetime
import random

date_list = [datetime.date(year=random.randint(2000, 2021), month=random.randint(1, 12), day=random.randint(1, 30))
             for i in range(12)]


'''
with open("dates", "w") as dates:
    writer = csv.writer(dates)
    writer.writerow(date_list)
'''


with open("dates", "r") as dates:
    reader = csv.reader(dates)
    reader = list(reader)
    min_d = reader[0][0]
    for i in reader[0]:
        if i < min_d:
            min_d = i
    print('Самая ранняя дата -', min_d)
