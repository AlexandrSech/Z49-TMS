"""
Дан файл, содержащий различные даты. Каждая дата - это число, месяц игод. Найти самую раннюю дату
"""
import csv
import datetime
import random

minsk = [
    {"Дата": datetime.date(year=random.randint(2000, 2021), month=random.randint(1, 12), day=random.randint(1, 30)),
     "Температура": random.randint(1, 30), "Скорость ветра": random.randint(0, 60)}
    for i in range(7)]

'''
with open("Minsk.csv", "w", newline="") as file:
    header = ["Дата", "Температура", "Скорость ветра"]
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(minsk)
'''


with open("Minsk.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    t = 0
    v = 0
    i = 0
    for row in reader:
        t += int(row["Температура"])
        v += int(row["Скорость ветра"])
        i += 1
    print("Минск:\nСредняя температура:", t / i, "\nСредняя скорость ветра:", v / i)
