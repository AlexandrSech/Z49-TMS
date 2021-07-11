from sqlalchemy import Column, Integer, String, ForeignKey
from globals import Base
from sqlalchemy.orm import relationship

'''
country
region
city
streets
'''


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Region(Base):
    __tablename__ = 'region'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    id_country = Column(Integer, ForeignKey('country.id'))
    country = relationship('Country', foreign_keys='Region.id_country')



