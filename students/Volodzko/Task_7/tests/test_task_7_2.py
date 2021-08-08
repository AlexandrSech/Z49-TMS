import unittest
from task_7_2 import *


class TestTask7_2(unittest.TestCase):
    def test_convert(self):
        self.assertRaises(ValueError,convert())
        self.assertEqual(convert(), 0)




if __name__ == '__main__':
    unittest.main()