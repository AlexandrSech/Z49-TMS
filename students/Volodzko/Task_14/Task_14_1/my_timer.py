class Timer:
    __first_name: str   # Имя
    __last_name: str    # Фамилия
    __hour: int         # Часы
    __minute: int       # Минуты
    __seconds: int      # секунды

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name.isalpha():
            self.__first_name = first_name
        else:
            print("Некоректно указано имя")

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name.isalpha():
            self.__last_name = last_name
        else:
            print("Некоректно указана фамилия")

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if hour <= 24 and hour >= 0:
            self.__hour = hour
        else:
            print("Количестов часов должно лежать в диапазоне: 0...24")

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        if minute <= 60 and minute >= 0:
            self.__minute = minute
        else:
            print("Количестов минут должно лежать в диапазоне: 0...60")

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds):
        if seconds <= 60 and seconds >= 0:
            self.__seconds = seconds
        else:
            print("Количестов часов должно лежать в диапазоне: 0...60")

    def __init__(self, first_name, last_name, hour, minute, seconds):
        self.first_name = first_name
        self.last_name = last_name
        self.hour = hour
        self.minute = minute
        self.seconds = seconds


    def logger(self, f_name, l_name, time_now):     # Метод логирования
        import csv
        with open("my_timer.log", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([f_name, l_name, f"{time_now[0]}, {time_now[1]}, {time_now[2]}, "
                                             f"{time_now[3]}:{time_now[4]}:{time_now[5]}"])

    def time_start(self):       # Старт таймера
        import time as tm
        from datetime import time
        from time import sleep
        self.logger(self.first_name, self.last_name, tm.localtime(tm.time()))
        t = time(self.hour, self.minute, self.seconds)
        result = t.hour * 3600 + t.minute * 60 + t.second   # Перевод введённого врремени в секунды

        while result > 0:
            h = result // 3600
            m = (result - h * 3600) // 60
            s = result - h * 3600 - m * 60
            print(f"{h}:{m}:{s}")
            result -= 1
            sleep(1)
        else:
            print("ALARM!!!!!")
