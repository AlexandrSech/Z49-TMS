import unittest
from Task_12_1.task_12_1 import *


class TestTask_12_1(unittest.TestCase):
    def my_object(self, h, m, s, h_r, m_r, s_r):
        time = MyTime(h, m, s)
        self.assertEqual(time.hours, h_r)
        self.assertEqual(time.minutes, m_r)
        self.assertEqual(time.seconds, s_r)

    def test_Mytime(self):
        self.my_object(10, 15, 17, 10, 15, 17)
        self.my_object(50, 70, 80, 3, 11, 20)
        self.my_object(-10, -20, -30, 13, 39, 30)
        self.my_object("10", "20", "30", 10, 20, 30)
        self.my_object("aa", "bb", "cc", None, None, None)

        """time = MyTime(10, 15, 17)

        self.assertEqual(time.hours, 10)
        self.assertEqual(time.minutes, 15)
        self.assertEqual(time.seconds, 17)

        time2 = MyTime(50,70,80)
        self.assertEqual(time2.hours, 3)
        self.assertEqual(time2.minutes, 11)
        self.assertEqual(time2.seconds, 20)

        time3 = MyTime(-10,-20,-30)
        self.assertEqual(time3.hours, 13)
        self.assertEqual(time3.minutes, 39)
        self.assertEqual(time3.seconds, 30)

        time4 = MyTime("10", "20", "30")
        self.assertEqual(time4.hours, 10)
        self.assertEqual(time4.minutes, 20)
        self.assertEqual(time4.seconds, 30)

        time5 = MyTime("aa", "bb", "cc")
        self.assertEqual(time5.hours, None)
        self.assertEqual(time5.minutes, None)
        self.assertEqual(time5.seconds, None)"""

    if __name__ == '__main__':
        unittest.main()
