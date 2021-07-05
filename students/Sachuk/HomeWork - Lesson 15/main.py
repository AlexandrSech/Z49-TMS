from task_15_1_my_class import my_psql

my_psql = my_psql()

#my_psql.connect_to_base('postgres', 'admin', 'tms_sql')
#my_psql.create_product('test', 0.0, 15, 'Test')
#my_psql.create_product('test2', 0.14, 999, 'Test2')
#my_psql.create_product('milk', 2.70, 56, 'Savushkin')
#my_psql.create_product('Chiken meat', 6.50, 45, 'Chiken meat')
#my_psql.create_product('Pork meat', 9.50, 64, 'Pork meat')
#my_psql.create_product('Coca-cola', 2.75, 88, 'Coca-cola')
#my_psql.create_product('Coca-cola without sugar', 2.99, 47, 'Coca-cola without sugar' )


my_psql.select_all()
my_psql.select_by(name='milk')
my_psql.select_by(id=3)
my_psql.update_by_id(4, new_name='KVAS')
my_psql.update_by_name('KVAS', new_name='BRED WATER', new_price=99.99)
my_psql.select_all()
#my_psql.delete_by_id(1)
#my_psql.select_all()
#my_psql.delete_by_name('test2')
#my_psql.select_all()
