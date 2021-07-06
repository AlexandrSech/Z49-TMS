from task_15 import Product

if __name__ == '__main__':
    print("CRUD")
    while True:
        print("Введите действие которое хотате выполнить:")
        x = int(input("1. Добавить новый продукт в таблицу\n2. Прочитать продукт\n"
                      "3. Обновить по id\n4. Удалить по id\n5. Выход "))
        if x == 1:
            names = input("Введите название нового продукта: ")
            price = float(input("Введите цену нового продукта: "))
            count = float(input("Введите количество нового продукта: "))
            comment = input("Введите комментарий для нового продукта: ")
            Product.create_prod(names, price, count, comment)
        if x == 2:
            Product.read_prod()

        if x == 3:
            id = input("Введите id продукта: ")
            Product.update_prod(id)

        if x == 4:
            id = input("Введите id продукта: ")
            Product.delete_prod(id)
        if x == 5:
            break

        else:
            continue
