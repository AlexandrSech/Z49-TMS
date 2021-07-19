import test_decorators.deco_example as dd
import unittest


class TestDeco(unittest.TestCase):

    def test_deco(self):
        dd.foo()
        self.assertNotEqual(dd.some_list_for_test_decorator_work, [])
        print(dd.some_list_for_test_decorator_work)

