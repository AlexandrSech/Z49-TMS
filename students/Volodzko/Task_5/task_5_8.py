"""
В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы
"""
my_string = "Ехал Грека через реку, видит Грека в реке рак."
my_list = list(my_string.split(" "))
my_list.reverse()
print(" ".join(my_list))

