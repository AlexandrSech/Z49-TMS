import datetime
import random
dict_trains = {}
names_dict = ["Номер поезда", "Посадка в", "Высадка в", "Время посадки", "Время высадки", ]
ii = 0
for train in range(1, 21):
    i = 0
    dict_train = {}
    train_number = random.randint(1000, 9999)
    point_in = "Москва"
    point_out = "Минск"
    time_out = (2021, 6, 6,
                str(random.randint(0, 23)) + ":" +
                                str(random.randint(0, 59)))
    time_in = (2021, 6, random.randint(6, 30),
                str(random.randint(0, 23)) + ":" +
                                str(random.randint(0, 59)))
    perem_dict = [train_number, point_in, point_out, time_out, time_in, ]
    for el in names_dict:
        dict_train[el] = perem_dict[i]
        i += 1
    dict_trains[ii+1] = dict_train
    ii += 1

for k, v in dict_trains.items():
    print(k, v)