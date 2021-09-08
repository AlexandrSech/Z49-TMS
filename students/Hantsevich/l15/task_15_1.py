"""
Создать таблицу продуктов.
Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для продуктов.
Создать пользовательский интерфейс.
"""

from sqlalchemy import create_engine, Column, String, Integer, FLOAT, MetaData, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///:bd1.db:', echo=True)
Base = declarative_base()
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()


class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Brand ('%s')>" % (self.name)

    class Car(Base):
        __tablename__ = 'cars'
        id = Column(Integer, primary_key=True)
        model = Column(String)
        r_year = Column(Integer)
        id_brand = Column(Integer, ForeignKey('brands.id'), nullable=False)

        cars = relationship('Brand', foreign_keys='Car.id_brand', backref='cars')

        def __repr__(self):
            return "<Car ('%s', '%d', '%d')>" % (self.model, self.relase_year, self.id_brand)

class Crud:
        """создание
        чтение
        обновление по id
        удаление по id"""


        def create_brand(self, brand_name):
                new_car = Car(name=brand_name)
                session.add(new_car)
                session.commit()

        def create_car(self, id_brand, model, release_year):
                new_car = Car(model=model, r_year=release_year, id_brand=id_brand)
                session.add(new_car)
                session.commit()


        # Функция для чтения моделей машин из таблицы Car
        def read_car(self, model_name):
            x = session.query(Car).filter_by(model=model_name).all()
            print(x)

        # Обновление по id
        def update_car(self, n_id):
            print("\n1. Модель\n"
                  "2. Год релиза\n"
                  "3. Бренд\n"
                  "0.Выход")
            s = int(input("Вевдите параметр, который хотите изменить: "))
            while True:
                if s == 1:
                    new_mod = input("Новое название модели: ")
                    m = session.query(Car).filter_by(id=n_id).first()
                    m.model = new_mod
                    session.commit()
                    break
                elif s == 2:
                    new_rel = input("Новый год релиза: ")
                    m = session.query(Car).filter_by(id=n_id).first()
                    m.relase_year = new_rel
                    session.commit()
                    break
                elif s == 3:
                    break

        def delete_car(self, n_id):
            session.query(Car).filter_by(id=n_id).delete()
            session.commit()


Base.metadata.create_all(engine)
