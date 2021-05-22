# В заданной строке расположить в обратном порядке все слова. Разделителями
# слов считаются пробелы. [02-7.2-HL08]

str = input('Please, enter the sentense: ')
print(str)
old_str = str.split()
new_str = reversed(old_str)
print(' '.join(new_str))