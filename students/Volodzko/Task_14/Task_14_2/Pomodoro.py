class Pomodoro:
    __first_name: str
    __last_name: str
    __focus: int
    __relax: int
    __number_of_cycles: int
    __task: str

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
    def focus(self):
        return self.__focus

    @focus.setter
    def focus(self, focus):
        try:
            self.__focus = int(focus)
        except:
            print("Не верно указано время фокусировки")

    @property
    def relax(self):
        return self.__relax

    @relax.setter
    def relax(self, relax):
        try:
            self.__relax = int(relax)
        except:
            print("Не верно указано время перерыва на отдыха")

    @property
    def number_of_cycles(self):
        return self.__number_of_cycles

    @number_of_cycles.setter
    def number_of_cycles(self, cycles):
        try:
            self.__number_of_cycles = int(cycles)
        except:
            print("Не коректно указано количество циклов")

    def __init__(self, first_name, last_name, task, focus=25, relax=5, number_of_cycles=4):
        self.first_name = first_name
        self.last_name = last_name
        self.focus = focus
        self.relax = relax
        self.number_of_cycles = number_of_cycles
        self.__task = task

    def logger(self, f_name, l_name, my_task, time_now):  # Метод логирования
        import csv
        with open("my_timer_pomodoro.log", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([f_name, l_name, my_task, f"{time_now[0]}, {time_now[1]}, {time_now[2]}, "
                                                      f"{time_now[3]}:{time_now[4]}:{time_now[5]}"])

    def time_start(self):  # Старт таймера
        import time as tm
        from time import sleep

        self.logger(self.first_name, self.last_name, self.__task, tm.localtime(tm.time()))

        while self.number_of_cycles >= 0:
            time_focus_value_second = self.focus * 60
            time_relax_value_second = self.relax * 60
            print("Сфокусируйся!)")
            while time_focus_value_second != 0:
                time_focus_value_second -= 1
                print(
                    f"{time_focus_value_second // 60}:{time_focus_value_second - (time_focus_value_second // 60) * 60}")
                sleep(1)
            print("Вермя немного отдахнуть)")
            while time_relax_value_second != 0:
                time_relax_value_second -= 1
                print(
                    f"{time_relax_value_second // 60}:{time_relax_value_second - (time_relax_value_second // 60) * 60}")
                sleep(1)

            self.number_of_cycles -= 1
        print("Конец")
