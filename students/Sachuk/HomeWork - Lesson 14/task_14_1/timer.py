"""
Написать программу таймер. Программа при запуске принимает имя,
фамилию, часы, минуты и секунды. После программа начинает обратный
отсчет выводя оставшееся время. Программа должна хранить файл
логирования с информацией о том кто запускал программу и когда.
Пример:
00:00:03
00:00:02
00:00:01
ALARM!!!
"""
import datetime
import time


class MyTimer:
    __first_name: str
    __last_name: str

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def log_file(self):
        with open('log.txt', 'a') as my_log:
            my_log.write(f'{self.first_name} {self.last_name} {str(datetime.datetime.now())} \n')

    def alarm(self, hours, minutes, seconds):
        self.log_file()
        count_of_seconds = hours * 3600 + minutes * 60 + seconds
        for i in range(count_of_seconds, -1, -1):
            if i == 0:
                print('ALARM!!!!!!')
            else:
                h = i // 3600
                m = (i % 3600) // 60
                s = (i % 3600) % 60
                print(f'{h}:{m}:{s}')
                time.sleep(1)
