import globals

import sqlalchemy
import models
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///map_db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# create
# globals.Base.metadata.create_all(engine)

# insert
'''r_id = 1
for c in range(1, 11):
    country = models.Country(id=c, name='Country_{}'.format(c))
    session.add(country)
    for _ in range(1, 11):
        region = models.Region(id=r_id, name='Region_{}_{}'.format(c, r_id), id_country=c)
        r_id += 1
        session.add(region)

session.commit()'''



# select
