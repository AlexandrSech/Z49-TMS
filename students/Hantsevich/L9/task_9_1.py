import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
lst =[get_random_string(i) for i in range(2, 5)]
lst2 = [str(i)+'-'+lst[i] for i in range(len(lst))]
print(lst, lst2)
