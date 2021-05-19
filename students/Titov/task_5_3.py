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


