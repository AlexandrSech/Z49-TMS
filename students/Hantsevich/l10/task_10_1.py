import csv
#Создание файла со списком людей
'''
lines = [['Имя','Фамилия','Возраст'],
        ['alexander', 'Brov', '42'],
        ['sfdsafa', 'fsadfs', '96'],
        ['sfdjfa', 'fsafdgdfs', '325'],
        ['shafa', 'fkjdfs', '320'],
        ['sfsdfa', 'fs34s', '17'],
        ['sfds76a', 'fsa8fs', '21'],
        ['sf98fa', 'fs98fs', '22']]

with open('people.csv', 'w') as f:
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
'''

#Анализ данных файла
with open('people.csv', 'r') as f:
    data = csv.reader(f)
    l1_12 = []
    l13_18 = []
    l19_25 = []
    l26_40 = []
    l40 = []

    for row in data:
        print(row)
        if int(row[2]) in range(1,13):
            l1_12.appennd(row)
        elif int(row[2]) in range(13, 19):
            l13_18.append(row)
        elif int(row[2]) in range(19, 26):
            l19_25.append(row)
        elif int(row[2]) in range(26, 40):
            l26_40.append(row)
        else:
            l40.append(row)

total = [["1-12", len(l1_12)],
["13-18", len(l13_18)],
["19-25", len(l19_25)],
["26-40", len(l26_40)],
["40+", len(l40)]]

#Создание фала отчета
'''
with open('peoplecount.csv', 'w') as f:
    writer = csv.writer(f)
    for line in total:
        writer.writerow(line)

'''



