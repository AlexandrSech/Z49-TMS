"""
Написать программу таймер. Программа при запуске принимает имя,
фамилию, часы, минуты и секунды. После программа начинает обратный
отсчет выводя оставшееся время. Программа должна хранить файл
логирования с информацией о том кто запускал программу и когда.
Пример :
00:00:03
00:00:02
00:00:01
ALARM!!!
"""

import time


class Timer:

    def __init__(self, hours: str, minutes: str, seconds: str, name):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.name = name

    def start(self):
        with open('log.txt', 'a') as file:
            file.write('{} by {}\n'.format(time.ctime(), self.name))

        result_time = int(self.hours) * 60 * 60 + int(self.minutes) * 60 + int(self.seconds)
        while result_time != -1:
            print('{:02}:{:02}:{:02}'.format(
                result_time // 3600,
                int(((result_time % 3600) - result_time % 60) / 60),
                result_time % 60))
            if result_time == 0:
                print('ALARM!!!')
            time.sleep(1)
            result_time -= 1


t1 = Timer('00', '02', '3', 'sdadasds')
t1.start()
