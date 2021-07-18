import unittest
from task_7_1 import *


class TestTask7(unittest.TestCase):

    def test_func1(self):
        self.assertEqual(func1(10), 25.4)
        self.assertEqual(func1(7), 17.78)
        self.assertEqual(func1('asfaf'), 'Введите число')
        self.assertEqual(func1('10'), 25.4)
        self.assertEqual(func1('1o'), 'Введите число')

    def test_func2(self):
        self.assertEqual(func2(10), 3.94)
        self.assertEqual(func2(7), 2.76)
        self.assertEqual(func2('asfaf'), 'Введите число')
        self.assertEqual(func2('10'), 3.94)
        self.assertEqual(func2('1o'), 'Введите число')

    def test_func3(self):
        self.assertEqual(func3(10), 16.1)
        self.assertEqual(func3(7), 11.27)
        self.assertEqual(func3('asfaf'), 'Введите число')
        self.assertEqual(func3('10'), 16.1)
        self.assertEqual(func3('1o'), 'Введите число')

    def test_func4(self):
        self.assertEqual(func4(10), 6.21)
        self.assertEqual(func4(7), 4.35)
        self.assertEqual(func4('asfaf'), 'Введите число')
        self.assertEqual(func4('10'), 6.21)
        self.assertEqual(func4('1o'), 'Введите число')

    def test_func5(self):
        self.assertEqual(func5(10), 4.535)
        self.assertEqual(func5(7), 3.1745)
        self.assertEqual(func5('asfaf'), 'Введите число')
        self.assertEqual(func5('10'), 4.535)
        self.assertEqual(func5('1o'), 'Введите число')

    def test_func6(self):
        self.assertEqual(func6(10), 22.0507)
        self.assertEqual(func6(7), 15.4355)
        self.assertEqual(func6('asfaf'), 'Введите число')
        self.assertEqual(func6('10'), 22.0507)
        self.assertEqual(func6('1o'), 'Введите число')

    def test_func7(self):
        self.assertEqual(func7(10), 283.5)
        self.assertEqual(func7(7), 198.45)
        self.assertEqual(func7('asfaf'), 'Введите число')
        self.assertEqual(func7('10'), 283.5)
        self.assertEqual(func7('1o'), 'Введите число')

    def test_func8(self):
        self.assertEqual(func8(10), 0.35)
        self.assertEqual(func8(7), 0.25)
        self.assertEqual(func8('asfaf'), 'Введите число')
        self.assertEqual(func8('10'), 0.35)
        self.assertEqual(func8('1o'), 'Введите число')

    def test_func9(self):
        self.assertEqual(func9(10), 45.46)
        self.assertEqual(func9(7), 31.822)
        self.assertEqual(func9('asfaf'), 'Введите число')
        self.assertEqual(func9('10'), 45.46)
        self.assertEqual(func9('1o'), 'Введите число')

    def test_func10(self):
        self.assertEqual(func10(10), 2.2)
        self.assertEqual(func10(7), 1.54)
        self.assertEqual(func10('asfaf'), 'Введите число')
        self.assertEqual(func10('10'), 2.2)
        self.assertEqual(func10('1o'), 'Введите число')

    def test_func11(self):
        self.assertEqual(func11(10), 5.683)
        self.assertEqual(func11(7), 3.9781)
        self.assertEqual(func11('asfaf'), 'Введите число')
        self.assertEqual(func11('10'), 5.683)
        self.assertEqual(func11('1o'), 'Введите число')

    def test_func12(self):
        self.assertEqual(func12(10), 17.5963)
        self.assertEqual(func12(7), 12.3174)
        self.assertEqual(func12('asfaf'), 'Введите число')
        self.assertEqual(func12('10'), 17.5963)
        self.assertEqual(func12('1o'), 'Введите число')


if __name__ == '__main__':
    unittest.main()
