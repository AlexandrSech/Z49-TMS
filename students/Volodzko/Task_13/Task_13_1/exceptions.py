"""Файл для создания собственных исключенй"""


class MyZeroException(Exception):  # Деление на ноль
    def __init__(self, text):
        super().__init__(text)


class MyValueException(Exception):  # Некоректное входное значение
    def __init__(self, text):
        super().__init__(text)
