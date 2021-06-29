'''
Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
год. Найти самую раннюю дату.
'''
import csv
import random
import datetime

dates = [datetime.date(day=random.randint(1, 28), month=random.randint(1, 12), year=random.randint(2010, 2020))
         for i in range(10)]
for i in dates:
    print(i)

with open('dates.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(dates)

with open("dates.csv", "r") as f:
    reader = csv.reader(f)
    reader = list(reader)
    print('min date =', min(reader[0]))



