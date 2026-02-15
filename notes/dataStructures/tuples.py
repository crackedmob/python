# TUPLES
mytuple = ('apple', 'banana', 'cherry')
# tuples are used to store multiple items in a single variable
# a tuple is a collection which is ordered and unchangeable
# tuples are written with round brackets
print(mytuple)


# tuple items
# tuple items re ordered, unchangeable, and allow duplicate values
# tuple items are indexed, the first item has index [0] , the second item
# has index [1] etc.


# ordered
# when we say that tuples are ordered, it means that the items have a defined
# order, and that order will not change

# unchangeable
# tuples are unchangeable, meaning that we cannot change, add or remove items
# after the tuple has been created


# allow duplicates
# since tuples are indexed, they can have items with the same value
thisistuple = ('apple', 'mango', 'cherry', 'apple', 'cherry')
print(thisistuple)


# tuple length
# we can use len() function to determine the number of items a tuple has
print(len(thisistuple))


# create tuple with one item
# to create a tuple with only one item , we have to add comma (,) after the item
# otherwise python will not recognize it as a tuple, but a string
newtuple = ('boss' ,)
print(type(newtuple))

# tuple can be of any data type : 
# string, int and boolean
tuple1 = ('apple', 'mango', 'cherry')
tuple2 = (1, 2, 4, 5, 8)
tuple3 = (True, False, False)
# a tuple can contain different data types
tuple4 = ('abs', 3, True) 

# tuples are defined as objects with the data type 'tuple'
# <class 'tuple'>
print(type(tuple1))

# the tuple() constructor
# it is also possible to use the tuple() constructor to make a tuple
newtuple1 = tuple(('abs', 'legs', 'chest'))
print(newtuple1)




# ACCESS TUPLE ITEMS
# e=we can access tuple items by referring to their index number, inside square brackets
print(newtuple1[1])


# negative indexing
# it means start from the end
# -1 refers to the last item , -2 refers to the second last item
print(newtuple1[-1])


# range of indexes
# we can specify a range of indexes by specifying where to start and where 
# to end the range
# when specifying a range, the return value will be a new tuple with 
# the specified items
print(newtuple1[0:2]) # the search will start at 0th index, and end at 2nd index(excluded)


# by leaving out the start value, the range will start at the first item
print(newtuple1[:2])

# by leaving out the end value, the range will go to the end of the tuple
print(newtuple1[0:])



# range of negative indexes
print(newtuple1[-3:-1])


# check if item exists
# we use in keyword for that
thisistuple = ('apple', 'mango', 'cherry', 'banana')
if "banana" in thisistuple:
    print("yes, 'banana' is in the tuple")


# UPDATE TUPLES
# tuples are unchangeable, meaning that you cannot change, add, or remove items
# once the tuple is created
# but there are some workarounds

# change tuple values
x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)

print(x)

# add items 
# since tuples are immutable, they do not have a built-in append() method,
# but there are other ways to add items to a tuple

# 1. Convert into a list : just like the workaround for changing a tuple, you can convert
# it into a list, add your item(s), and onvert it back into a tuple
y = list(thisistuple)
y.append('orange')
thisistuple = tuple(y)
print(thisistuple)

# 2. Add tuple to a tuple : we are allowed to add tuples , so if you 
# want to add one item, (or many) , create a new tuple with the items(s)
# and add it to the existing tuple
y = ('orange',)
thisistuple += y
print(thisistuple)




# Remove Items
# we cannot remove items in a tuple
# tuples are unchangeable, so we cannit remove items from it, but we can 
# use the same workaround as we used for changingn and adding tuple items
thisistuple = ('apple', 'mango', 'banana', 'cherry')
y = list(thisistuple)
y.remove('apple')
thisistuple = tuple(y)
print(thisistuple)


# or we cann delete the tuple completely
# the del keyword can delete the tuple completely
#thisistuple = ('apple', 'mango', 'cherry')
#del thisistuple
#print(thisistuple)# this raises an error because the tuple is no longer 





# UNPACK TUPLES
# unpacking a tuple : when we create a tuple, we normally assign values to it. This is
# called "packing" a tuple
fruits = ('mango', 'apple', 'cherry')
# same way we are also allowed to extract the values back into variables.
# this is called 'unpacking'
fruits = ('apple', 'mango', 'cherry')

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
# the number of variables must match the number of values in the tuple, if not, you must
# use an asterisk to collect the remaining values as a list


# using asterisk*
# if the number of variables is less than the number of values, you can add an *
# to the variable name and the values will be assigned to the variable as a list
fruits = ('apple', 'mango', 'cherry', 'banana', 'pineapple', 'melon')
(green, blue, *red) = fruits
print(blue)
print(green)
print(red)
# if the asterisk is added to any other variable name than the last, 
# the values will be assigned to the variable until the number of values left matches
# the number of variables left
(green, *tropic, red) = fruits
print(tropic)
print(green)
print(red)




# loop tuples
thisistuple = ('apple', 'mango', 'cherry')
for x in thisistuple:
    print(x)


# loop through the index numbers
# using range() and len() functions to create a suitable iterable
thisistuple = ('banana', 'pineappple', 'orange')
for x  in range(len(thisistuple)):
    print(thisistuple[x])



# using a while loop
# use a len() function to determine the length of the tuple,
# then start at 0 and loop your way through the tuple
# items by referring to their indexes
i = 0
while i < len(thisistuple):
    print(thisistuple[i])
    i = i + 1



# JOIN TUPLES
# we can use + operator to join two or more tuples
tuple1 = ('a','b', 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)



# multiply tuples
# if we want to multiply the content of a tuple a given number of times, you can use the 
# * operator
fruits = ('apple', 'mango', 'cherry')
mytuple = fruits * 2
print(mytuple)



# TUPLE METHODS
# 1. count() : returns the number of times a specified value occurs in a tuple
# 2. index() : searches the tuple for a specified value and returns the 
#              position of where it was found