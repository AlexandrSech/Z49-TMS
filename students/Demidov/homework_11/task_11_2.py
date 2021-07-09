class Car():

    mark: str
    model: str
    year: int
    speed: int

    def __init__(self, mark, model, year, speed=0):
        self.mark = mark
        self.model = model
        self.year = year
        self.speed = speed

    def boost(self):
        self.speed += 5
        return self.speed

    def slow_down(self):
        self.speed -= 5
        return self.speed

    def stop(self):
        self.speed = 0
        return self.speed

    def show_speed(self):
        return print(self.speed)



bmw3 = Car("BMW", "BMW3", 2019)

bmw3.boost()
bmw3.boost()
bmw3.slow_down()
bmw3.slow_down()
bmw3.slow_down()
bmw3.slow_down()
bmw3.stop()
bmw3.slow_down()


bmw3.show_speed()

bmw3.boost()