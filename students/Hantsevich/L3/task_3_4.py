word = input()
l = len(word)
mid = l // 2
print(word[(mid-1)])
if word[(mid-1)] == word[0]:
    print(word[1:(l - 1)])