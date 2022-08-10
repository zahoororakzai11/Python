# #if statements
#
# x = int(input("Please enter an integer: "))
#
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# # else:
# #     print('More')
# #


# #function return a list of numbers
# def fib2(n):
#     result = []
#     a,b = 0,1
#     while a < n:
#         result.append(a)
#         a,b = b, a + b
#     return result

# print(fib2(100))


# list(range(3, 6))            # normal call with separate arguments

# args = [3, 6]
# print(list(range(*args)))            # call with arguments unpacked from a list

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_1))
print(list(list_1))

# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
	for arg in argv:
		print (arg)
	
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

print(list(range(3, 6)))
  

