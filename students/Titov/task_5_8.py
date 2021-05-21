'''В заданной строке расположить в обратном порядке все слова. Разделителями
слов считаются пробелы'''
stroka = 'rfr lmjnj asdfjn [weon wffdsgm we[qw[ sdfm'
spis = stroka.split(' ')
new_stroka = ''
print(spis)
for el in reversed(range(len(spis))):
    new_stroka = (new_stroka + ' '+ spis[el])
print(new_stroka)

