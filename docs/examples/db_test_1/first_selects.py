from classes import Holiday
from sqlalchemy import create_engine



# connection to DB
my_engine = create_engine("sqlite:///first_db.db")

hol = Holiday(my_engine).select_all()

for line in hol:
    print(line)








'''co_list = []
with open('commands.txt') as co:
    co_list = co.read().splitlines()


for co in co_list:
    my_engine.execute(co)'''


'''
r = my_engine.execute('select * from holiday where id == 32;')

for line in r:
    print(line)
'''
