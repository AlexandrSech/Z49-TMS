# type of data

# string

ms = "123a sdfsf fdsf dsf"

print(ms)

text = '''
ok, man
'''
text2 = 'one\ntwo\nthree'

print(ms.split(' '))
print(ms.splitlines()) # ms.split('\n') - the same
print(type(text))
print(text2)
print(text2.splitlines())

# print(dir(ms)) - show all methods

simple_list = ['one', 'two', 'three']
simple_list_second = [1, 2, 3, 4, 5]
print('->'.join((simple_list)))
print('->'.join(map(str, simple_list_second)))
print('Hello, World! I like cheese'.replace('cheese', 'bread'))

ex1 = 'my simple text'
print(ex1)
ex1 = ex1.capitalize()
print(ex1)

a = '345674655'
new_a = [a[i:i+3] for i in range(0, len(a), 3)]
print(new_a)