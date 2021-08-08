import unittest
from task_8_2 import *

class TestTask_8_2(unittest.TestCase):
    def test_my_polindrom(self):
        self.assertEqual(my_polindrom("Коту тащат уток"), 'Полиндром')
        self.assertEqual(my_polindrom("Коту тащиииит уток"), 'Не полиндром')
        self.assertEqual(my_polindrom(123), 'Не полиндром')


