

####********************************Methods to Perform Operation on Lists*************************************########

#Native Method
# initializing list
var_list = [1,2,3,4,5,6,7,8,9]
print ("Original list is : " + str(var_list))
# using naive method to
# get index and value
print("List with index-values are:")
for i in range(len(var_list)):
    print(i, end="")
    print(i)

#list comprehension
list_name = ['zahoor','Javid','Murtaza']
print("Original List:" +str(list_name))
print(list_name)
print("List with index and values:")
print ([list((i, list_name[i])) for i in range(len(list_name))])

#Using enumerate()
'''most elegant method to perform and highly recommended to be
used in case we required to get index along with value'''

list_alphabats = ['a','b','c','d','e']
print("Original list is:" +str(list_alphabats))
print("List with enumrata method")
for index,value in enumerate(list_alphabats):
    print(index,value)

# #Using Zip Method
test = ['a','b','zahoor','minha']
#Printing list
print("Original list is: " +str(test))
#using zip method
#get index and values
for index, value in zip(range(len(test)),test):
    print(index,value)

