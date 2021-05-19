my_dict = {

}

print(my_dict)
my_dict['name'] = 'Totoshka'
my_dict['users'] = ['Tim', 'Helen', 'Vlad']
my_dict['another_dict'] = {'name': 'Tom'}

print(my_dict['name'])
print(my_dict['users'])
print(my_dict['another_dict']['name'])


print(my_dict.values())
print(my_dict.keys())
print(my_dict.items())

email = 'lskasasakk@dsdksdlsd.ndc'
if '@' in email:
    index_at = email.split('@')
    print(index_at)

if '.' in index_at[1]:
    print(index_at[-1].split('.'), len(index_at[-1].split('.')))
    if len(index_at[-1].split('.')[-1]) > 1:
        print(True)
    else:
        print(False)