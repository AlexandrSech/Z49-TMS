'''Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300.'''


for i in range(200,30001):
    ch_1 = 0
    ch_2 = 0
    for el in range(1, i): #220
        if i % el == 0:
            ch_1 += el
    for al in range(1, ch_1):
        if ch_1 % al == 0:
            ch_2 += al
    if ch_1 != ch_2 and ch_2 == i and ch_2 < ch_1:
        print(ch_2, ch_1)






exit()
spis = []
spis_1 = []
mnozh = set()
spis_2 = []
for el in range(220, 1220): #220
    spis.clear()
    for el_1 in range(1, el):
        if el % el_1 == 0:
            spis.append(el_1)
    for al in range(220, 1220): #284
        mnozh.clear()
        spis_1.clear()
        chislo_1 = 0
        chislo_2 = 0
        for al_1 in range(1, al ):
            if al % al_1 == 0:
                spis_1.append(al_1)
        for el_2 in range(len(spis)):
            chislo_1 += spis[el_2]
        for al_2 in range(len(spis_1)):
            chislo_2 += spis_1[al_2]
        if chislo_1 == al and chislo_2 == el and chislo_2 != chislo_1:
            mnozh.add(chislo_1)
            mnozh.add(chislo_2)
    print(mnozh)

            #print(chislo_1, chislo_2)


