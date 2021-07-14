from globals import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    relase_year = Column(Integer)
    id_brand = Column(Integer, ForeignKey('brands.id'), nullable=False)

    # cars = relationship('Brand', foreign_keys='Car.id_brand', backref='cars')

    def __repr__(self):
        return "<Car ('%s', '%d', '%d')>" % (self.model, self.relase_year, self.id_brand)
