n1=1
n2=2
oper='symbol'

while oper != 0:
	n1 = input('Введите число 1: ')
	while not str.isdigit (n1):
		print('ошибка')
		n1 = input('Введите число 1: ')
	n2 = input('Введите число 2: ')
	while not str.isdigit (n2):
	    print('ошибка')
	    n2 = input('Введите число 2: ')
	oper = input('Введите операцию: ')
	if oper == '0':
	   exit()
	elif oper == '+':
	   print (float(n1)+float(n2))
	elif oper == '-':
	    print (float(n1)-float(n2))
	elif oper == '*':
	    print (float(n1)*float(n2))
	elif oper == '/':
	    if n2 == '0':
	    	print ('Деление на ноль невозможно')
	    else:
	        print (float(n1)/float(n2))
	else:
	     print('Неверная операция')