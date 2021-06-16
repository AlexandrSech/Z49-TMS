
def foo(spis = []):
    spis_1 = []
    spis_2 = []
    number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    print(number_names[0])
    for i in spis:
        print(i, type(int(i)))
        if 0 <= int(i) and int(i) < 20:
            spis_2.append(number_names[int(i)])
    spis_2 = sorted(spis_2)
    for el in range(len(spis_2)):
        for i in number_names:
            if number_names[i] == spis_2[el]:
                spis_1.append(i)
    return spis_1
stdin = '0 1 1 2 3 5 8 13'
spis = list(stdin.split(' '))
m = str(foo(spis))
print(m.replace('[', '').replace(']', '').replace(',', ''))


exit()
def foo(spis = []):
    spis_1 = []
    spis_2 = []
    number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    for i in spis:
        spis_2.append(number_names[int(i)])
    spis_2 = sorted(spis_2)
    for el in range(len(spis_2)):
        for i in number_names:
            if number_names[i] == spis_2[el]:
                spis_1.append(i)
    return spis_1
stdin = '0 1 1 2 3 5 8 13'
spis = list(stdin.split())
m = str(foo(spis))
print(m.replace('[', '').replace(']', '').replace(',', ''))