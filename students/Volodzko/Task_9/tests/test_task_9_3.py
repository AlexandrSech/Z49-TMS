import unittest
from task_9_3 import *


""""
Как протестировать работу декоратора"""
class TestTask_9_3(unittest.TestCase):
    def test_func(self):
        self.assertEqual(func([1,2,3,4,5]), [1,3,5])
        self.assertEqual(func(["a",2,3,True,5]), ["a",3,True, 5])