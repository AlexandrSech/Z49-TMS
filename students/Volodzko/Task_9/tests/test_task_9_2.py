import unittest
from task_9_2 import *


class TestTask_9_2(unittest.TestCase):
    def test_my_dict_power(self):
        self.assertEqual(my_dict_power(abc=5, bb=7), {'abcabc': 5, 'bbbb': 7})
        self.assertEqual(my_dict_power(a=1), {'aa': 1})
