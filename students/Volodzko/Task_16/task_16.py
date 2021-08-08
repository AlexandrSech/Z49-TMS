import globals
from models.Brand import Brand
from models.Car import Car
from sqlalchemy import create_engine

from sqlalchemy.orm.session import sessionmaker

DB_User = "postgres"
DB_Name = "Cars"
DB_Pasward = "postgres"
DB_Echo = True

engine = create_engine(f'postgresql://{DB_User}:{DB_Pasward}@localhost/{DB_Name}', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# globals.Base.metadata.create_all(engine)

mers = Brand(name="Mercedes")
bmw = Brand(name="BMW")
toyota = Brand(name="Toyota")
audi = Brand(name="Audi")

w210 = Car(model='W210', relase_year=1995, id_brand=1)
w211 = Car(model='W211', relase_year=2002, id_brand=1)
w212 = Car(model='W212', relase_year=2009, id_brand=1)

x5 = Car(model='X5', relase_year=1999, id_brand=2)
x6 = Car(model='X6', relase_year=2008, id_brand=2)
x7 = Car(model='X7', relase_year=2018, id_brand=2)

q5 = Car(model='Q5', relase_year=2008, id_brand=3)
q7 = Car(model='Q7', relase_year=2005, id_brand=3)
q8 = Car(model='Q8', relase_year=2018, id_brand=3)

camry = Car(model='Camry', relase_year=1991, id_brand=4)
corolla = Car(model='Corolla', relase_year=1966, id_brand=4)
land_cruser = Car(model='Land_Cruser', relase_year=1951, id_brand=4)

"""session.add(mers)
session.add(bmw)
session.add(audi)
session.add(toyota)
session.commit()"""

"""session.add(w210)
session.add(w211)
session.add(w212)
session.add(x5)
session.add(x6)
session.add(x7)
session.add(q5)
session.add(q7)
session.add(q8)
session.add(camry)
session.add(corolla)
session.add(land_cruser)
session.commit()
"""

"""session.query(Brand).filter(id == 1).delete()"""
