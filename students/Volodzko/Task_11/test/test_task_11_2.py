import unittest
from task_11_2 import *


class Test_Task_11_2(unittest.TestCase):
    def test_Car(self):
        car = Car("BMW", "X5", 2009, 200)
        self.assertEqual(car.mark, "BMW")
        self.assertEqual(car.model, "X5")
        self.assertEqual(car.year, 2009)
        self.assertEqual(car.speed, 200)

        car.mark = 111
        self.assertEqual(car.mark, '')

        car.year = 'sdad'
        self.assertEqual(car.year, 0)

        car.speed = 'dfs'
        self.assertEqual(car.speed, 0)

        car.speed = 25
        self.assertEqual(car.speed, 25)

        car.speed = -25
        self.assertEqual(car.speed, 0)

        car.speed = 7
        self.assertEqual(car.speed, 7)

        self.assertEqual(car.speed_dec(), 2)
        self.assertEqual(car.speed_dec(), 0)
