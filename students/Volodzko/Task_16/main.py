from Crud import Crud

"""
Создать таблицы Brand(name), Car(model, release_year, brand(foreing key на таблицу Brand)).
Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для бренда и машины.
Создать пользовательский интерфейс.
"""

if __name__ == '__main__':
    c = Crud()
    print("CRUD")
    while True:
        print("Введите действие которое хотате выполнить:")
        x = int(input("1. Добавить новый автомобидь в таблицу\n2. Прочитать автомобиль\n"
                      "3. Обновить по id\n4. Удалить по id\n5. Выход "))

        if x == 1:
            b_name = input("Введите название бренда (Mercedes, Audi, Toyota, BMW): ")
            c_year = input("Введите год релиза ")
            mod = input("Введите название модели ")
            c.create_car(model=mod, relase_y=c_year, brand_name=b_name)

        elif x == 2:
            try:
                mod = input("Введите название модели: ")
                c.read_car(mod)
            except:
                print("Такой модели нет в базе")

        elif x == 3:
            mod = int(input("Введите id: "))
            c.update_car(mod)

        elif x == 4:
            id = int(input("Введите id: "))
            c.delete_car(id)

        elif x == 5:
            break
