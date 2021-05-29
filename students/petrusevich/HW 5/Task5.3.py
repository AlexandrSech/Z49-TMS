def get_friedly_numebrs():
    d = {}
    for n in range(200, 301):
        temp_list = []
        for delitel in range(1, n):
            if n % delitel == 0:
                temp_list.append(delitel)
        d[n] = sum(temp_list)
        #print(n, d[n])
        #print(n, temp_list)
    tl = []
    for k in d:
        if d[k] in d and d[d[k]] == k:
            if k not in tl:
                tl.append(k)
                tl.append((k)
    print(k, d[k])

r = get_friedly_numebrs()