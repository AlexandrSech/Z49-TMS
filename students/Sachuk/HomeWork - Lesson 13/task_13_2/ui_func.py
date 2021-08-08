from classes import Calculate

def ui_func():
    my_calc = Calculate()
    print('Консольный простой калькулятор')
    while True:
            a = my_calc.number_validation()
            my_calc.get_a = a
            b = my_calc.number_validation()
            my_calc.get_b = b
            operator = my_calc.operation_validation()
            my_calc.get_result = operator
            print(my_calc.get_result)

