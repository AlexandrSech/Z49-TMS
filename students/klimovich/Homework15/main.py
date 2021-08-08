import pyodbc
from datetime import datetime
'''
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для продуктов.
Создать пользовательский интерфейс.
'''


class Sql:
    def __init__(self, database, server="DESKTOP-OVIDSIB"):
        self.cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                   "Server=" + server + ";"
                                                        "Database=" + database + ";"
                                                                               "Trusted_Connection=yes;")

        self.cursor = self.cnxn.cursor()


    def write_query(self, query: str):
        for n, row in enumerate(list(self.cursor.execute(query))):
            print(n, row)
        self.cursor.commit()


try:
    sql = Sql('homework15')
    print('Подключено')
except Exception:
    print('Не подключился чел')



while True:
    print('1. вывести таблицу Products')
    print('2. удалить строку из таблицы')
    print('3. написать запрос')
    print('0. выход')
    sign = input('введите номер: ')
    if sign == '1':
        sql.write_query('select * from Products')
    if sign == '2':
        try:
            ss = input('Введите id строки: ')
            sql.write_query('delete Products where id={}'.format(ss))
        except Exception:
            print('Походу такой строки нет')
    if sign == '3':
        query = input('напишите запрос: ')
        sql.write_query(query)
    if sign == '0':
        break

