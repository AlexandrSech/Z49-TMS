"""
Создать программу Pomodoro.
На вход программа получает имя, фамилию, время для
фокусировки(по-умолчанию 25 минут), длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи. Программа указывает
оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки. Программа должна
вести файл лога о всех запусках.
"""
import time


class Pomodoro:
    name: str
    focus_time: int
    b_time: int
    cycles: int
    task_name: str

    def __init__(self, name, task_name, focus_time=1, b_time=2, cycles=3):

        self.name = name
        self.task_name = task_name
        self.focus_time = focus_time
        self.b_time = b_time
        self.cycles = cycles

    def logger(self, a):
        with open('log2.txt', 'a') as file:
            file.write(a)

    def start_timer(self):
        self.logger('{}: Запуск {}  -  {}\n'.format(self.name, self.task_name, time.ctime()))
        print(self.task_name)

        for i in range(1, self.cycles + 1):
            print('Цикл {}! Работай раб, солнце еще высоко!!!'.format(i))
            self.logger('{}({}): Цикл {}  -  {}\n'.format(self.name, self.task_name, i, time.ctime()))
            s = self.focus_time * 60
            for j in range(s, -1, -1):
                print('{:02}:{:02}:{:02}'.format(
                    s // 3600, (s % 3600) // 60, (s % 3600) % 60))
                # time.sleep(1)
                s -= 1

            print('Перерыв {} минут ! Парам-Пам-Пам-Пам!!  '.format(self.b_time))
            self.logger('{}({}): Перерыв {} минут  -  {}\n'.format(self.name, self.task_name,
                                                                   self.b_time, time.ctime()))
            tm_time = self.b_time * 60
            for k in range(tm_time, -1, -1):
                m = tm_time // 60 - 60
                if m < 0:
                    m += 60
                print('{:02}:{:02}:{:02}'.format(
                    tm_time // 3600, (tm_time % 3600) // 60, (tm_time % 3600) % 60))
                # time.sleep(1)
                tm_time -= 1
        self.logger('{}({}): Окончание работы  -  {}\n'.format(self.name, self.task_name, time.ctime()))


r = Pomodoro('ilijah', 'My_task', 3, 1, 2)
r.start_timer()
