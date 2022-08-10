"""my_list = [1,2,3,4]

list_ = [x**2 for x in my_list]
print(list_)"""
#same thing we can do with generator

"""my_list = [1,2,3,4]
generator = (x**2 for x in my_list)
print(next(generator))
"""


"""def factorial(x):
  if x == 1:
    return 1
  else:
    return x * factorial(x - 1)


print(factorial(5))"""


def sum_to(x):
  return x + sum_to(x - 1)


print(sum_to(5))