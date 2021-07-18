import unittest
from task_8_1 import *


class TestTask_8_1(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(fact(10), (945, 3840))
        self.assertEqual(fact('10'), (945, 3840))
        self.assertEqual(fact('aafasda'), ('Введено не число'))
