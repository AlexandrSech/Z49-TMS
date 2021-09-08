"""
Создать таблицу продуктов.
Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для продуктов.
Создать пользовательский интерфейс.
"""
from task_15_1 import Products

if __name__ == '__main__':
    print("CRUD")
    while True:
        print("Введите действие которое хотате выполнить:")
        x = int(input("1. Добавить новый продукт в таблицу\n"
                      "2. Прочитать продукт\n"
                      "3. Прочитать Все\n"
                      "4. Обновить по id\n"
                      "5. Удалить по id\n"
                      "0. Выход\n"
                      "Enter:"))
        if x == 1:
            name = input("Введите название нового продукта: ")
            price = float(input("Введите цену нового продукта: "))
            count = float(input("Введите количество нового продукта: "))
            comments = input("Введите комментарий для нового продукта: ")
            Products.add_prod(name, price, count, comments)
        if x == 2:
            Products.read_prod()

        if x == 3:
            Products.read_all()

        if x == 4:
            id = int(input("Введите id продукта: "))
            Products.upd_by_id(id)

        if x == 5:
            id = int(input("Введите id продукта: "))
            Products.delete_prod(id)
        if x == 0:
            break

        else:
            continue
