# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной
# длины. {‘abc’: 5} -> {‘abcabc’: 5}

def foo(**kwargs):
  my_dict = {}
  for k, v in kwargs.items():
    new_keys = lambda old_keys: old_keys * 2
    my_dict[new_keys(k)] = v
  return my_dict

print(foo(abc=10))