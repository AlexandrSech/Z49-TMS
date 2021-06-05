import csv
import datetime

"""
Создать csv файл с данными о ежедневной погоде. Структура:
Дата,Место, Градусы, Скорость ветра. Найти среднюю погоду
(скорость ветра иградусы) для Минск за последние 7 дней
"""

waters_Minsk = [
    {"Дата": datetime.date(year=2021, month=5, day=29), "Температура": 17, "Скорость ветра": 4},
    {"Дата": datetime.date(year=2021, month=5, day=30), "Температура": 17, "Скорость ветра": 4},
    {"Дата": datetime.date(year=2021, month=5, day=31), "Температура": 14, "Скорость ветра": 2},
    {"Дата": datetime.date(year=2021, month=6, day=1), "Температура": 15, "Скорость ветра": 2},
    {"Дата": datetime.date(year=2021, month=6, day=2), "Температура": 20, "Скорость ветра": 5},
    {"Дата": datetime.date(year=2021, month=6, day=3), "Температура": 21, "Скорость ветра": 3},
    {"Дата": datetime.date(year=2021, month=6, day=4), "Температура": 21, "Скорость ветра": 2}
]
waters_Kiev= [
    {"Дата": datetime.date(year=2021, month=5, day=29), "Температура": 18, "Скорость ветра": 4},
    {"Дата": datetime.date(year=2021, month=5, day=30), "Температура": 15, "Скорость ветра": 5},
    {"Дата": datetime.date(year=2021, month=5, day=31), "Температура": 14, "Скорость ветра": 5},
    {"Дата": datetime.date(year=2021, month=6, day=1), "Температура": 15, "Скорость ветра": 8},
    {"Дата": datetime.date(year=2021, month=6, day=2), "Температура": 16, "Скорость ветра": 7},
    {"Дата": datetime.date(year=2021, month=6, day=3), "Температура": 20, "Скорость ветра": 7},
    {"Дата": datetime.date(year=2021, month=6, day=4), "Температура": 22, "Скорость ветра": 5}
]
waters_Moscow= [
    {"Дата": datetime.date(year=2021, month=5, day=29), "Температура": 14, "Скорость ветра": 3},
    {"Дата": datetime.date(year=2021, month=5, day=30), "Температура": 14, "Скорость ветра": 3},
    {"Дата": datetime.date(year=2021, month=5, day=31), "Температура": 13, "Скорость ветра": 2},
    {"Дата": datetime.date(year=2021, month=6, day=1), "Температура": 17, "Скорость ветра": 1},
    {"Дата": datetime.date(year=2021, month=6, day=2), "Температура": 21, "Скорость ветра": 2},
    {"Дата": datetime.date(year=2021, month=6, day=3), "Температура": 20, "Скорость ветра": 2},
    {"Дата": datetime.date(year=2021, month=6, day=4), "Температура": 23, "Скорость ветра": 2}
]

with open("water_Minsk.csv", "w", newline="") as file:
    header = ["Дата", "Температура", "Скорость ветра"]
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(waters_Minsk)

with open("water_Kiev.csv", "w", newline="") as file:
    header = ["Дата", "Температура", "Скорость ветра"]
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(waters_Minsk)

with open("water_Moscow.csv", "w", newline="") as file:
    header = ["Дата", "Температура", "Скорость ветра"]
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(waters_Minsk)

with open("water_Minsk.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    t = 0
    v = 0
    i=0
    for row in reader:
        t += int(row["Температура"])
        v += int(row["Скорость ветра"])
        i+=1
    print(f"Минск:\nСредняя температура: {round(t/i,1)}\nСредняя скорость ветра: {round(v/i,1)} ")

