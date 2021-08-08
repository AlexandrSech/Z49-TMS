"""
Создать программу Pomodoro.
На вход программа получает имя, фамилию, время для
фокусировки(по-умолчанию 25 минут), длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи. Программа указывает
оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки. Программа должна
вести файл лога о всех запусках.
"""
import datetime
import time


class Pomidoro:
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
            my_log.write(f'{self.first_name} {self.last_name} {str(datetime.datetime.now())}')

    def pomidoro(self, task_name='', focus_time=25, timeout=5, count_of_circle=4):
        self.log_file()
        for i in range(1, count_of_circle + 1):
            print(task_name + ' circle ' + str(i))
            for time_to_work in range(focus_time * 60, -1, -1):

                if time_to_work == 0:
                    yield 'NOW RELAX - TIMEOUT'
                else:
                    print(f'{time_to_work // 60}:{time_to_work % 60}')
                    time.sleep(0.1)

            if i == count_of_circle:
                break

            for time_to_relax in range(timeout * 60, -1, -1):
                if time_to_relax == 0:
                        yield 'NOW TIME TO WORK'
                else:
                    print(f'{time_to_relax // 60}:{time_to_relax % 60}')
                    time.sleep(0.1)