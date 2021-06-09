stroka = str(input("Введите любой текст: \n"))
stroka_new = ""
stroka = stroka.lower()
list_stroka = stroka.split()
for el in range(len(list_stroka)):
    stroka_new += str(list_stroka[-el - 1]) + " "
print(stroka_new)