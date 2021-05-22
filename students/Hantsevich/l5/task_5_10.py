import datetime

my_d ={"1": ("a", datetime.datetime(2021, 1, 10, 22, 57), "b", datetime.datetime(2021, 1, 11, 1, 57)),
       "2": ("d", datetime.datetime(2021, 2, 7, 10, 57), "c", datetime.datetime(2021, 2, 7, 22, 11)),
       "3": ("e", datetime.datetime(2021, 3, 2, 1, 57), 'g', datetime.datetime(2021, 3, 2, 22, 11))}


for i in my_d.keys():
    a = my_d[i][3] - my_d[i][1]
    if a > datetime.timedelta(0, 26400):
        print(my_d[i])