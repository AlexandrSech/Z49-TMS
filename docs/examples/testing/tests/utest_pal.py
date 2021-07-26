import unittest
import pal
import random


class GetPal(unittest.TestCase):

    def test_check_result_get_pal(self):
        self.assertEqual(pal.get_pal('aaba'), 'aabaa')
        self.assertEqual(pal.get_pal('mama'), 'mamam')
        self.assertEqual(pal.get_pal('aa'), 'aa')
        self.assertEqual(pal.get_pal('a'), 'a')
        self.assertEqual(pal.get_pal(''), '')
        self.assertEqual(pal.get_pal(123), '12321')
        self.assertEqual(pal.get_pal(101), '101')

    def test_other_types_in_arg(self):
        self.assertRaises(TypeError, pal.get_pal({}))
        self.assertRaises(Exception, pal.get_pal({}), '{}')

