import unittest
from task_9_4 import *


""""
Как протестировать работу декоратора"""
class TestTask_9_4(unittest.TestCase):
    def test_func(self):
        self.assertEqual(func(1,2,3), (3,2,1))
        self.assertEqual(func("1", 2, 3), (3, 2, '1'))