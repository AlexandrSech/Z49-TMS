from exceptions import DigitException, OperationException, ZeroException


class Calculate:
    __a: int
    __b: int
    __result: int

    @property
    def get_a(self):
        return self.__a

    @get_a.setter
    def get_a(self, a):
        self.__a = a

    @property
    def get_b(self):
        return self.__b

    @get_b.setter
    def get_b(self, b):
        self.__b = b

    @property
    def get_result(self):
        return self.__result

    @get_result.setter
    def get_result(self, result):
        self.__result = result

    def summ(self):
        return self.get_a + self.get_b

    def subtraction(self):
        return self.get_a - self.get_b

    def multiply(self):
        return self.get_a * self.get_b

    def division(self):
        return self.get_a / self.get_b

    def number_validation(self):
        while True:
                a = input('Введите число: ')
                if (a[0] == '-' and a[1::].isdigit()) or  a.isdigit():
                    break
                else:
                    raise DigitException("Вы ввели не число")
        return int(a)

    def operation_validation(self):
        while True:
            list_operators = ['-', '+', '*', '/']
            a = input('Введите операцию + - / * : ')
            if a in list_operators:
                break
            else:
                raise OperationException("Введена не корректная операция")
        if a == '-':
            return self.subtraction()
        if a == '+':
            return self.summ()
        if a == '*':
            return self.multiply()
        if a == '/':
            if self.get_b != 0:
                return self.division()
            else:
                raise ZeroException("Деление на 0 запрещено")
