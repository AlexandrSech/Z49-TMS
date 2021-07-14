from globals import Base
from sqlalchemy import Column, String, Integer


class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Brand ('%s')>" % (self.name)
