# В семье N свадьба. Они решили выбрать заведение, где будут праздновать в
# зависимости от количества людей, которое прибудет к утру.
# Если их будет больше 50 - закажут ресторан, если от 20 до 50 -то кафе, а если
# меньше 20 то отпраздную дома.
# Вывести "ресторан", "кафе", "дом" в зависимости от количества гостей (прочитать
# переменную с консоли)

num = int(input())

if num > 50:
    print('ресторан')
elif num >= 20 and num <= 50:
    print("кафе")
elif num > 0 and num < 20:
    print('дом')
else:
    print('Будет очень скучная свадьба :(')

