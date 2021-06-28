from exceptions import *
from func import *


def ui_func():
    print('Консольный простой калькулятор')
    while True:
        a = number_validation()
        b = number_validation()
        c = operation_validation(a, b)
        print(c)
