import unittest
from task_9_1 import *

class TestTask_9_1(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(),['0 - Черный Мерседес', '1 - Синяй БМВ', '2 - Зелёная Ауди'])