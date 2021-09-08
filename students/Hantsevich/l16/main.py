"""
Создать таблицы Brand(name), Car(model, release_year, brand(foreing key на таблицу Brand)).
Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для бренда и машины.
Создать пользовательский интерфейс.
"""


from models import *

if __name__ == '__main__':
    c = Crud()
    print("CRUD")
    while True:
        print("Введите действие которое хотате выполнить:")
        a = int(input("1. Работа с Брендами\n"
                      "2. Работа с авто\n"
                      "0. Выход "))

        if a == 1:
            while True:
                x = int(input("1. Добавить новый Бренд\n"
                              "2. Прочитать Бренды\n"
                              "3. Обновить по id\n"
                              "4. Удалить по id\n"
                              "5. Выход "))
                if x == 1:
                    b_name = input("Введите название бренда : ")
                    c.create_brand(brand_name=b_name)

                elif x == 2:
                    print(c.read_brand())

                elif x == 3:
                    mod = int(input("Введите id: "))
                    c.update_brand(mod)

                elif x == 4:
                    id = int(input("Введите id: "))
                    c.delete_brand(id)

                elif x == 5:
                    break
        if a == 2:
            while True:
                x = int(input("1. Добавить новый авто\n"
                              "2. Прочитать авто\n"
                              "3. Прочитать все\n"
                              "4. Обновить по id\n"
                              "5. Удалить по id\n"
                              
                              "0. Выход "))
                if x == 1:
                    b_name = input("Введите id бренда {}: ".format(c.read_brand()))
                    c_year = input("Введите год релиза ")
                    mod = input("Введите название модели ")
                    c.create_car(id_brand=b_name, model=mod, release_year=c_year)

                elif x == 2:
                    c.read_car()

                elif x == 3:
                    c.read_all_car()

                elif x == 4:
                    mod = int(input("Введите id: "))
                    c.update_car(mod)

                elif x == 5:
                    id = int(input("Введите id: "))
                    c.delete_car(id)

                elif x == 0:
                    break