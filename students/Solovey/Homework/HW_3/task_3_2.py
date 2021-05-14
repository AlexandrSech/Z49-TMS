guests = int(input('Enter guests quantity:'))
if guests > 50:
    print('Restaurant')
elif guests > 20 and guests < 50:
    print('Cafe')
else: print('Home')
