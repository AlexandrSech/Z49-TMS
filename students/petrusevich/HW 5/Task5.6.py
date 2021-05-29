a = [43, 56, 56, 67, 67, 78, 79, 80, 0, 89]
rez = 0
flag = False
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        flag = True
    else:
        if flag:
            rez += 1
            flag = False
print(rez)