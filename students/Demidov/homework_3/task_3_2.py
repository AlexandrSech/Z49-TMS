guests = int(input("Введите число гостей: "))

if guests > 50:
    print("restaurant")
elif 20 <= guests <= 50:
    print("cafe")
else:
    print("house")