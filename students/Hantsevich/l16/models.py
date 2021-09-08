"""
Создать таблицы Brand(name), Car(model, release_year, brand(foreing key на таблицу Brand)).
Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для бренда и машины.
Создать пользовательский интерфейс.
"""

from sqlalchemy import create_engine, Column, String, Integer, FLOAT, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///Cars.db', echo=True)
Base = declarative_base()
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()


class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    def __repr__(self):
        return "<Brand ('%s')>" % (self.name)


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String)
    r_year = Column(Integer)
    id_brand = Column(Integer, ForeignKey('brands.id'), nullable=False)

    cars = relationship('Brand', foreign_keys='Car.id_brand', backref='cars')

    def __repr__(self):
        return "<Car ('%s', '%d', '%d')>" % (self.model, self.r_year, self.id_brand)


class Crud:
    """создание
        чтение
        обновление по id
        удаление по id"""

    def create_brand(self, brand_name):
        new_br = Brand(name=brand_name)
        session.add(new_br)
        session.commit()

    def create_car(self, id_brand, model, release_year):
        new_car = Car(model=model, r_year=release_year, id_brand=id_brand)
        session.add(new_car)
        session.commit()


    def read_car(self):
        try:
            mod = int(input("Введите id: "))
            x = session.query(Car).filter(Car.id == mod).all()
            print(x)
        except:
            print("Такой модели нет в базе")

    def read_all_car(self):
        x = session.query(Car).order_by(Car.id)
        for item in x:
            print(item.id, item.model, item.r_year, item.id_brand)

    def read_brand(self):
        x = session.query(Brand).order_by(Brand.id)
        for item in x:
            print(item.id, item.name)

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
                m.r_year = new_rel
                session.commit()
                break
            elif s == 3:
                new_br = input("Введите id бренда: ")
                m = session.query(Car).filter_by(id=n_id).first()
                m.id_brand = new_br
                session.commit()
                break
            elif s == 0:
                break

    def update_brand(self, n_id):
        new_br = input("Новое название модели: ")
        m = session.query(Brand).filter_by(id=n_id).first()
        m.name = new_br

    def delete_car(self, n_id):
        session.query(Car).filter_by(id=n_id).delete()
        session.commit()

    def delete_brand(self, b_id):
        session.query(Brand).filter_by(id=b_id).delete()
        session.commit()


Base.metadata.create_all(engine)
