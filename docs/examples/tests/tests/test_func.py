import unittest
from func import palindrom1


class Pal1(unittest.TestCase):

    def test_pal(self):
        self.assertEqual(palindrom1('mama'), 'mamam')
        self.assertEqual(palindrom1('aaba'), 'aaba')

    def test_pal2(self):
        self.assertRaises(ValueError, palindrom1(''))


