'''
Создать csv файл с данными следующей структуры: Имя, Фамилия,
Возраст. Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
19-25, 26-40, 40+
'''

import csv

rows = [['Имя','Фамилия','Возраст'],
        ['first', 'qaz', '15'],
        ['second', 'fserhgb', '24'],
        ['third', 'kfgyjfgb', '6'],
        ['fourth', 'piyoyr', '77'],
        ['fifth', 'mnbvcxz', '22'],
        ['sixth', 'pokjhgfcxs', '33'],
        ['seventh', 'kjhradfvdgfgj', '30'],
        ['eighth', 'jkfhgjkebvjkb', '41']]


with open('people.cvs', 'w') as my_file:
    file_writer = csv.writer(my_file, delimiter=',')
    file_writer.writerows(rows)

with open('people.cvs', 'r') as my_file:
    reader = csv.reader(my_file, delimiter=',')

# Шаблон для отчетного файла
    result = [['1-12', 0],
    ['13-18', 0],
    ['19-25', 0],
    ['26-40', 0],
    ['40+', 0]]

    for row in reader:
        if row[2] == 'Возраст':
            pass
        elif int(row[2]) in range(1,13):
            result[0][1] += 1
        elif int(row[2]) in range(13, 19):
            result[1][1] += 1
        elif int(row[2])  in range(19, 26):
            result[2][1] += 1
        elif int(row[2])  in range(26, 41):
            result[3][1] += 1
        else:
            result[4][1] += 1

with open('result_count.cvs', 'w') as res:
    wr = csv.writer(res, delimiter=',')
    wr.writerows(result)