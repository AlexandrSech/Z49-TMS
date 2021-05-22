# Написать 12 функций по переводу:

# Дюймы в сантиметры
# Сантиметры в дюймы
# Мили в километры
# Километры в мили
# Фунты в килограммы
# Килограммы в фунты
# Унции в граммы
# Граммы в унции
# Галлон в литры
# Литры в галлоны
# Пинты в литры
# Литры в пинты

def number():
    while True:
        x = input('Please, enter the number: ')
        if x.isdigit():
            break
        else:
            print(' I TOLD YOU!!!!!READ CAREFULLY!!! Enter the number: ')
    return x


def conversion():
    print('Welcome to my little console conversion! Enter the number and get rusult.\n'
          '1 - Дюймы в сантиметры\n'
          '2 - Дюймы в сантиметры\n'
          '3 - Сантиметры в дюймы\n'
          '4 - Мили в километры\n'
          '5 - Километры в мили\n'
          '6 - Фунты в килограммы\n'
          '7 - Килограммы в фунты\n'
          '8 - Унции в граммы\n'
          '9 - Граммы в унции\n'
          '10 - Литры в галлоны\n'
          '11 - Пинты в литры\n'
          '12 - Литры в пинты\n')
    while True:
        choice = number()
        if choice == '0':
            print("Noooooooooooooooo, please COME BACK!!!!! How did you know how to get out of here?\n "
                  "Don't tell me you read the assignment carefully")
            break
        elif int(choice) > 0 and int(choice) <= 12:
            print('How many units do you want to convert?')
            y = number()
            y = int(y)
            convetation = {}
            convetation['1'] = y * 2.54
            convetation['2'] = y * 0.39
            convetation['3'] = y * 1.6
            convetation['4'] = y * 0.62
            convetation['5'] = y * 0.0003048
            convetation['6'] = y * 3280.84
            convetation['7'] = y * 28.3495
            convetation['8'] = y * 0.035274
            convetation['9'] = y * 3.78541
            convetation['10'] = y * 0.264172
            convetation['11'] = y * 0.473176
            convetation['12'] = y * 2.11338
            print(f'Your result is equal      : {convetation[choice]} \n We start a new conversion!\n'
                  f'There is no way out of here (c) John Cramer!!! Aha-ha-ha-ha!. Look UP!')

print(conversion())