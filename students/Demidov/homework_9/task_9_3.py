def decorator(func):
  def wrapper(my_list):
    func(my_list)
    return [i for i in my_list if i % 2 != 0]
  return wrapper


@decorator
def foo(my_list: list):
  return my_list

print(foo([1, 3, 10, 6, 8, 4]))