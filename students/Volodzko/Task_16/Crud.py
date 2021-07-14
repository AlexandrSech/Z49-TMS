from models.Car import Car
from models.Brand import Brand
from task_16 import session


class Crud:
    """создание
    чтение
    обновление по id
    удаление по id"""

    # метод создания новой машины используя уже существующие бренды
    def create_car(self, model, relase_y, brand_name):
        if brand_name == 'Mercedes':
            new_car = Car(model=model, relase_year=relase_y, id_brand=1)
            session.add(new_car)
            session.commit()
        elif brand_name == 'BMW':
            brand = Brand(id=2, name=brand_name)
            new_car = Car(model=model, relase_year=relase_y, id_brand=2)
            session.add(new_car)
            session.commit()
        elif brand_name == 'Audi':
            brand = Brand(id=4, name=brand_name)
            new_car = Car(model=model, relase_year=relase_y, id_brand=3)
            session.add(new_car)
            session.commit()
        elif brand_name == 'Toyota':
            brand = Brand(id=3, name=brand_name)
            new_car = Car(model=model, relase_year=relase_y, id_brand=4)
            session.add(new_car)
            session.commit()

    # Функция для чтения моделей машин из таблицы Car
    def read_car(self, model_name):
        x = session.query(Car).filter_by(model=model_name).all()
        print(x)

    # Обновление по id
    def update_car(self, n_id):
        print("\n1. Модель\n2. Год релиза\n3. Выход")
        s = int(input("Вевдите параметр, который хотите изменить: "))
        while True:
            if s == 1:
                new_mod = input("Введите новое название модели: ")
                m = session.query(Car).filter_by(id=n_id).first()
                m.model = new_mod
                session.commit()
                break
            elif s == 2:
                new_rel = input("Введите новое значение года релиза: ")
                m = session.query(Car).filter_by(id=n_id).first()
                m.relase_year = new_rel
                session.commit()
                break
            elif s == 3:
                break

    # Удаление по id
    def delete_car(self, n_id):
        session.query(Car).filter_by(id=n_id).delete()
        session.commit()
