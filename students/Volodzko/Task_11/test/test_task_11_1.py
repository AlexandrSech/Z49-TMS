import unittest
from task_11_1 import *

class TestTask_11_1(unittest.TestCase):

    def test_Dod(self):
        dog = Dog(11, 25, "Charley")
        self.assertEqual(dog.name, 'Charley')
        self.assertEqual(dog.weight, 11)
        self.assertEqual(dog.height, 25)

        dog2 = Dog('lkmlm', "re", "ds1")

        self.assertEqual(dog2.weight, 0)
        print(dog2.weight)

        self.assertEqual(dog2.height, 0)

        self.assertEqual(dog2.name, '')
