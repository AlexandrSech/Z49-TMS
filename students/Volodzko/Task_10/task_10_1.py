import csv
import json

"""
Создать csv файл с данными следующей структуры: Имя, Фамилия,Возраст. 
Создать отчетный файл с информацией по количеству людейвходящих в 
ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,19-25, 26-40, 40+.
"""
file_name = "task_10_1.csv"
file_name2 = "task_10_1_2.json"
users = [
    {"first_name": "Tom", "last_name": "Carick", "age": 28},
    {"first_name": "Alice", "last_name": "Tramp", "age": 23},
    {"first_name": "Bob", "last_name": "Woodly", "age": 34},
    {"first_name": "Phill", "last_name": "Mask", "age": 8},
    {"first_name": "Stiven", "last_name": "Jobs", "age": 22},
    {"first_name": "Ronny", "last_name": "Salivan", "age": 41}
]
"""
Создаём csv файл, запичываем в него hrader и список словарей содержащие: Имя, Фамилию и возраст!
В результате получаем таблицу, где headeh - это шапка, а список словарей - это значения.
"""
with open(file_name, "w") as file:
    header = ["first_name", "last_name", "age"]
    csvwriter = csv.DictWriter(file, fieldnames=header)
    csvwriter.writeheader()
    csvwriter.writerows(users)

"""
Создаём json файл, где будут храниться данные из списка users отсортированные по возрасту.
"""
with open(file_name2, "w") as file2:
    with open(file_name, "r") as file:  # Открываем csv файл и считываем данные из таблицы
        reader = csv.DictReader(file)
        age_dict = {"1-12": 0, "13-18": 0, "19-25": 0, '26-40': 0, "40+": 0}
        for i in reader:  # Сортируем данные из таблицы
            if int(i["age"]) < 12:
                age_dict["1-12"] += 1
            elif 19 > int(i["age"]) > 12:
                age_dict["13-18"] += 1
            elif 26 > int(i["age"]) > 19:
                age_dict["19-25"] += 1
            elif 40 > int(i["age"]) > 26:
                age_dict["26-40"] += 1
            elif int(i["age"]) > 40:
                age_dict["40+"] += 1

        for key, value in age_dict.items():
            data = json.dumps(f"{key} : {value}")
            file2.writelines(data)  # Записываем отсортированную таблицу в файл json
            file2.write("\n")
