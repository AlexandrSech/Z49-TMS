word = input()
l = len(word)
mid = l // 2
if word[mid] == word[0]:
    print(word[:mid])
else:
	print(word[(mid)])