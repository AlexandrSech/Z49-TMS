import csv
from my_reader_csv import my_reader
'''1. Создать csv файл с данными следующей структуры: Имя, Фамилия,
Возраст. Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
19-25, 26-40, 40+.
'''

with open('venv/my_csv_file.csv', 'r') as file:
    result_of_func = my_reader(file.read())
    print(result_of_func)
    my_dict = {}
    text = ''
    for i in range(len(result_of_func)):
        print(result_of_func[i][2])
        if int(result_of_func[i][2]) > 18 and int(result_of_func[i][2]) < 26:
            text += result_of_func[i][0] + ' '
        my_dict['18-25'] = text
    print(my_dict)