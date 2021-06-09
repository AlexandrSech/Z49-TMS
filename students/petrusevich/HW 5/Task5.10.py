import datetime

poezda = {
    'poezd1': [123, 'Smorgon', datetime.datetime(2021, 5, 13, 19, 44), 'Minsk', datetime.datetime(2021, 5, 12, 7, 6)],
    'poezd2': [321, 'Тверь', datetime.datetime(2021, 6, 13, 13, 44), 'Новгород',
               datetime.datetime(2021, 5, 12, 14, 32)],
    'poezd3': [234, 'Москва', datetime.datetime(2021, 5, 13, 19, 44), 'Воронеж', datetime.datetime(2021, 5, 12, 14, 32)]
    }
for i in poezda.keys():
    a = datetime.timedelta(0, 26400)
    b = poezda[i][2] - poezda[i][4]
    if b > a:
        print(poezda[i])
    else:
        pass
