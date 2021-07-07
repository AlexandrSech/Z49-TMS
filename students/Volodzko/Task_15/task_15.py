from sqlalchemy import create_engine, Column, String, Integer, FLOAT, MetaData, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

"""
Создать таблицу продуктов.
Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для продуктов.
Создать пользовательский интерфейс.
"""
engine = create_engine('sqlite:///ProductDB.db', echo=True)  # Подключение к базе, echho=True - отражает все запросы
base = declarative_base()  # класс от которого будут наследоваться ORM классы (для декларативного мапинга)
session = sessionmaker(bind=engine)()  # создание сессии

metadata = MetaData()

"""Создание таблицы"""
"""product = Table('products', metadata, 
                Column('id', Integer, primary_key=True),
                Column('name_product', String),
                Column('price', FLOAT),
                Column('count', FLOAT),
                Column('Comment', String))

metadata.create_all(engine)"""  # cretate_all - создаёт таблицу


class Product(base):
    """Создание таблицы 2 способ"""
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name_product = Column(String)
    price = Column(FLOAT)
    count = Column(FLOAT)
    comment = Column(String)

    def __repr__(self):
        return "<Product('%s', '%f', '%f', '%s')>" % \
               (self.name_product, self.price, self.count, self.comment)

    """Фнкция добавления данных в таблицу"""

    @classmethod
    def create_prod(cls, name, price, count, comment=""):
        session.add(Product(name_product=name, price=price, count=count, comment=comment))  # Добавляем новый объект
        session.commit()  # Вносим изменения в таблицу

    """Фнкция удаления данных из таблицы по id"""

    @classmethod
    def delete_prod(cls, id):
        session.query(Product).filter(Product.id == id).delete()
        session.commit()

    """Фнкция чтения данных из таблицы по названию"""

    @classmethod
    def read_prod(cls):
        s = input("Введите название продукта, которое хотите прочитать: ")
        x = session.query(Product).filter(Product.name_product == s).all()
        print(x)

    """Фнкция изменения данных в таблице по id"""

    @classmethod
    def update_prod(cls, id):
        """Функция update принимает 2 праметра: словарь
        ключём которого является параметр, который надо изменить в таблице,
        а значением параметр который будет являться новым значением в таблице,
        synchronize_session=False - описание стратегии обнавления атрибутов"""

        while True:
            print("1.Название продукта\n2.Цена\n3.Количество\n4.Выход\n")
            s = input("Введите параметр который хотите изменить: ")
            if s == "1":
                n_new = input("Введите новое название продукта: ")
                session.query(Product).filter(Product.id == id).update(
                    {Product.name_product: n_new},
                    synchronize_session=False)
                session.commit()

            if s == "2":
                p_new = input("Введите новую цену продукта: ")
                session.query(Product).filter(Product.id == id).update(
                    {Product.price: p_new},
                    synchronize_session=False)
                session.commit()

            if s == "3":
                c_new = input("Введите новое количество продукта: ")
                session.query(Product).filter(Product.id == id).update(
                    {Product.count: c_new},
                    synchronize_session=False)
                session.commit()

            if s == "4":
                break


base.metadata.create_all(engine)
