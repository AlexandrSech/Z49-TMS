from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task_15_1_alchemy import Products


class my_psql:
    __engine = None
    __session = None

    @property
    def session(self):
        return self.__session

    @session.setter
    def session(self, session):
        self.__session = session

    def connect_to_base(self, db_user, db_password, db):
        self.__engine = create_engine(f'postgresql://{db_user}:{db_password}@localhost/{db}', echo=False)
        self.__session = sessionmaker(bind=self.__engine)()
        print(f'Connect to base is succsessful. Session{self.__session} is create')

    def create_product(self, name: str, price: float, count=0, comment=None):
        product = Products(name=name, price=price, count=count, comment=comment)
        self.session.add(product)
        self.session.commit()
        print("Add product is successful")

    def select_all(self):
        query = self.session.query(Products).order_by(Products.id)
        for item in query:
            print(item.id, item.name, item.price, item.count, item.comment)

    def select_by(self, id=None, name=None):
        if id:
            item = self.session.query(Products).filter(Products.id == id).first()
            print(item.id, item.name, item.price, item.count, item.comment)

        elif name:
            item = self.session.query(Products).filter(Products.name == name).first()
            print(item.id, item.name, item.price, item.count, item.comment)

    def update_by_id(self, id, new_name=None, new_price=None, new_count=None, new_comment=None):
        print('UPDATE BY ID START')
        item = self.session.query(Products).filter(Products.id == id).first()
        print(item.id, item.name, item.price, item.count, item.comment)
        if new_name:
            item.name = new_name
        if new_price:
            item.price = new_price
        if new_count:
            item.count = new_count
        if new_comment:
            item.comment = new_comment
        print(item.id, item.name, item.price, item.count, item.comment)
        print('UPDATE BY ID FINISH')
        self.session.commit()

    def update_by_name(self, name, new_name=None, new_price=None, new_count=None, new_comment=None):
        print('UPDATE BY NAME START')
        item = self.session.query(Products).filter(Products.name == name).first()
        print(item.id, item.name, item.price, item.count, item.comment)
        if new_name:
            item.name = new_name
        if new_price:
            item.price = new_price
        if new_count:
            item.count = new_count
        if new_comment:
            item.comment = new_comment
        print(item.id, item.name, item.price, item.count, item.comment)
        print('UPDATE BY NAME FINISH')
        self.session.commit()

    def delete_by_id(self, id):
        print('DELETE BY ID IS START')
        item = self.session.query(Products).filter(Products.id == id).first()
        self.session.delete(item)
        print('DELETE BY ID IS FINISHED')
        self.session.commit()

    def delete_by_name(self, name):
        print('DELETE BY NAME IS START')
        item = self.session.query(Products).filter(Products.name == name).first()
        self.session.delete(item)
        print('DELETE BY NAME IS FINISHED')
        self.session.commit()

