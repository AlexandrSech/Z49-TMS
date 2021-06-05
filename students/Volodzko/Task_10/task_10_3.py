import csv
import datetime
import random

"""
Дан файл, содержащий различные даты. Каждая дата - это число, месяц игод. Найти самую раннюю дату
"""
date_list = [datetime.date(year=random.randint(2000, 2021), month=random.randint(1, 12), day=random.randint(1, 30)),
             datetime.date(year=random.randint(2000, 2021), month=random.randint(1, 12), day=random.randint(1, 30)),
             datetime.date(year=random.randint(2000, 2021), month=random.randint(1, 12), day=random.randint(1, 30)),
             datetime.date(year=random.randint(2000, 2021), month=random.randint(1, 12), day=random.randint(1, 30)),
             datetime.date(year=random.randint(2000, 2021), month=random.randint(1, 12), day=random.randint(1, 30)),
             datetime.date(year=random.randint(2000, 2021), month=random.randint(1, 12), day=random.randint(1, 30)),
             datetime.date(year=random.randint(2000, 2021), month=random.randint(1, 12), day=random.randint(1, 30)),
             datetime.date(year=random.randint(2000, 2021), month=random.randint(1, 12), day=random.randint(1, 30)),
             datetime.date(year=random.randint(2000, 2021), month=random.randint(1, 12), day=random.randint(1, 30)),
             datetime.date(year=random.randint(2000, 2021), month=random.randint(1, 12), day=random.randint(1, 30)),
             ]
with open("my_file", "w") as file:
    writer = csv.writer(file)
    writer.writerow(date_list)

with open("my_file", "r") as file:
    reader = csv.reader(file)
    reader = list(reader)
    minimum = reader[0][0]
    for i in reader[0]:
        if i < minimum:
            minimum = i
    print(minimum)
