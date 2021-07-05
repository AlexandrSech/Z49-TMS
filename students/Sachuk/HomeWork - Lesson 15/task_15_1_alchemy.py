from sqlalchemy import create_engine, Column, Integer, String, DECIMAL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_user = 'postgres'
db_password = 'admin'
db = 'tms_sql'

engine = create_engine(
    f'postgresql://{db_user}:{db_password}@localhost/{db}',
    echo=False,
)

Session = sessionmaker(bind=engine)  # объект, через который я буду управлять данными, чтением и отправкой в базу
session = Session()

Base = declarative_base()


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True)
    price = Column(DECIMAL)
    count = Column(Integer)
    comment = Column(String)

Base.metadata.create_all(engine)
