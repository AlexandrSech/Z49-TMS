import unittest
from unittest.mock import MagicMock
from palindrom import Palindrom


class PalTests(unittest.TestCase):

    def test_get_pal(self):
        pp = Palindrom()
        self.assertEqual(pp.get_pal({}), '{}{')
        self.assertEqual(pp.get_pal('aa'), 'aa')

    def test_gp(self):
        pp = Palindrom()
        pp.get_pal = MagicMock(return_value='abcd')
        self.assertEqual(pp.get_pal(''), '')

