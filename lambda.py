"""triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))
"""

#lambda function to multiple 2 with list items
"""list_number = [11, 22, 33]
result = list(map(lambda x: x * 2, list_number))
print(result)
"""
#lambda function using filter to remove item when don't match with condition

numbers = [11,22,33,44,55,60,35,25]
result_filter = list(filter(lambda x: x% 2 == 0,numbers))
print("Filter Will remove items that doesn't match with condition ")
print(result_filter)

def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

print(next(PowTwoGen()))
