import time


class Promodoro:
    name: str
    time_for_focus: int
    timeout: int
    cycles: int
    name_of_task: str

    def __init__(self, name, name_of_task, time_for_focus=25, timeout=5, cycles=4):
        self.cycles = cycles
        self.name = name
        self.timeout = timeout
        self.time_for_focus = time_for_focus
        self.name_of_task = name_of_task

    def start(self):
        self.logger('запуск программы Promodoro-{} в {}\n'.format(self.name_of_task, time.localtime()))

        print('TASK {}'.format(self.name_of_task))
        for i in range(1, self.cycles+1):
            print('Cycle num {}!!!'.format(i))
            s = self.time_for_focus * 60
            for j in range(s, -1, -1):
                m = s // 60 - 60
                if m < 0:
                    m += 60
                print('{:02}:{:02}:{:02}'.format(
                    s // 3600,
                    m,
                    s % 60
                ))
                time.sleep(1)
                s -= 1

            print('---Timeout is about {} minute---'.format(self.timeout))
            t_s = self.timeout * 60
            for k in range(t_s, -1, -1):
                m = t_s // 60 - 60
                if m < 0:
                    m += 60
                print('{:02}:{:02}:{:02}'.format(
                    t_s // 3600,
                    m,
                    t_s % 60
                ))
                time.sleep(1)
                t_s -= 1


    def logger(self, s):
        with open('log2.txt', 'a') as file:
            file.write(s)


t1 = Promodoro('Evgeniy', 'DoHomework')
t1.start()