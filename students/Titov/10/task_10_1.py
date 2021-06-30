'''Создать csv файл с данными следующей структуры: Имя, Фамилия,
Возраст. Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
19-25, 26-40, 40+.'''

import csv

users =[
    ['name', 'secname', 'age'],
    ['Tom', 'Holand', 29],
    ['Martin', 'Zebra', 12],
    ['Malmen', 'Jiraf', 10],
    ['Glorya', 'Begemot', 34],
    ['Brad', 'Pit', 54],
    ['Mike', 'Vazovski', 7]
]
kolvo = [
    ['1-12', '13-18', '19-25', '26-40', 40]
]
spis = [0 for i in range(5)]
with open("first.csv", "w+") as f_file: #Записываем изначальные данные людей
    writer = csv.writer(f_file)
    writer.writerows(users)

with open('first_zap.csv', 'w+') as firstzap_file: #Записываем кол-во человек того или иного возратса
    writer_1 = csv.writer(firstzap_file)
    writer_1.writerows(kolvo)
    with open('first.csv', 'r') as f_file: #Считываем людей из файла и заносим в список в соответствии с возрастом
        reader = csv.DictReader(f_file)
        for row in reader:
            a = int(row['age'])
            if a >= 1 and a <= 12:
                spis[0] += 1
            elif a >= 13  and a <= 18 :
                spis[1] += 1
            elif a >= 19 and a <= 25:
                spis[2] += 1
            elif a >= 26 and a <= 40:
                spis[3] += 1
            elif a > 40:
                spis[4] += 1
    writer_1.writerow(spis)
    firstzap_file.seek(0)
    reader_1 = csv.reader(firstzap_file)
    for row in reader_1:
        print(row)

