word = input()
l = len(word)
mid = l // 2

if word[(mid)] == word[0]:
    print(word[:(l)])
else:
    print(word[(mid-1)])