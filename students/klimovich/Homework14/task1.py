import time


class Timer:
    def __init__(self, hours: str, minutes: str, seconds: str, name):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.name = name

    def print_time(self):
        self.hours = int(self.hours)
        self.minutes = int(self.minutes)
        self.seconds = int(self.seconds)
        print('Таймер: {:02}:{:02}:{:02}'.format(self.hours, self.minutes, self.seconds))

    def start_timer(self):
        result_time = int(self.hours) * 60 * 60 + int(self.minutes) * 60 + int(self.seconds)
        for i in range(result_time, -1, -1):

            m = result_time // 60 - 60
            if m < 0:
                m += 60
            print('{:02}:{:02}:{:02}'.format(
                result_time // 3600,
                m,
                result_time % 60
            ))
            if result_time == 0:
                print('ALARM!!!')
            # time.sleep(1)
            result_time -= 1

    def write_to_file(self):
        with open('log.txt', 'a') as file:
            file.write('{}:{}:{} by {}\n'.format(self.hours, self.minutes, self.seconds, self.name))


t1 = Timer('01', '02', '3', 'Evgeniy')
t1.print_time()
t1.start_timer()
t1.write_to_file()