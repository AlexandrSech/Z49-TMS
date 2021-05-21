london = {
      'id': 1,
      'name': 'London',
      'it_vlan': 320,
      'user_vlan': 1010,
      'mngmt_vlan': 99,
      'to_name': None,
      'to_id': None,
      'port': 'G1/0/11'
}

print('London' in london)

print(london.get('sdf', 0))




exit()

sss = 'asdfvnsek sdkvjnsdfjvn sdfv sdf'

splitter = sss.split(' ')

print(splitter)

splitter = splitter[::-1]


exit()

print('\n'.join(splitter))

rr = sss.replace(' ', '_')
print(rr)


exit()


n = [1,2,3,4,5,6]

first, *_, last = n

print(first, last)

a = b = c = 1

print(a, b, c)

exit()
if n > m:
      print('n > m')
elif n == m:
      print('n == m')
elif n < m:
      print('n < m')
else:
      print('else')


exit()


sss = 'sdfgvsdfvs'

print(sss[len(sss) - 2])
print(sss[-1])
print(sss[0:-2])
print(sss[0::2])
exit()

london = {
      'id': 1,
      'name': 'London',
      'it_vlan': 320,
      'user_vlan': 1010,
      'mngmt_vlan': 99,
      'to_name': None,
      'to_id': None,
      'port': 'G1/0/11'
}

print(london['port'])

exit()

my_set = {1,2,3,4,}
ms2 = set(['a', 'b', ])
print(ms2)
# ms2.add(['b'])
ms2.add('c')
print(ms2)
exit()

my_tuple = (1,2,3,4,)
mt2 = tuple([1,2,3,])

print(mt2.append(1))

exit()


m = [[]] * 3
n = [[], [], []]

# print(m)

m[1].append(123)

print(m)

for i in m:
      print(id(i))

exit()

my_list1 = [1,2,34,4,]
my_list2 = list('hello world')
print(my_list2)

my_list1.append('qwewerwert')

print(my_list1[4])

print(my_list1.pop(0))
print(my_list1)

print(my_list1[::-1])



exit()

i = 10

print(i, id(i))

i += 1
print(i, id(i))


exit()

first_name = 'foo'
last_name = 'bar'
age = 120

print('Привет\n, меня зовут ' + first_name + ' ' + last_name +
      ', мне ' + str(age) + ' лет.')

print('Привет, меня зовут {} {}, мне {} лет.'.
      format(first_name, last_name, age))

exit()

my_string = 'asfsvsdfvsfv'
my_int = int('12')

my_float = float()

my_string2 = str('dfgsgsdf')

my_str = str(my_int)

print(my_str)

print(type((True)))

print(type(my_float))


