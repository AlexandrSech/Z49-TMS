peoples = int(input("Сколько будет гостей: "))
if peoples > 50:
    print("Ресторан")
elif peoples >= 20 and peoples <= 50:
    print("Кафе")
else: print("Дома")