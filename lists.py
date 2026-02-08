# LISTS
mylist = ['apple', 'banana', 'cherry']
# lists are used to store multiple items in a single variable
# there are only 4 built-in datatypes in python used to store collections of data
# 1. list : is a collection which is ordered and changeable.
#           Allows duplicate members.
# 2. tuple : is a collection which is ordered and unchangeable.
#           Allows duplicate members.
# 3. set : is a collection which is unordered, unchangeable, and unindexed.
#           No duplicate
# 4. dictionary : is a collection which is ordered and changeable.
#               No duplicate members.

# lists are created using square brackets
thisislist = ['king' , ' queen' , 'slave']
print(thisislist)

# list items are ordered, changeable, and allow duplicate values
# list items are indexed, the first item has index [0],  the second item has index [1] etc


# ORDERED
# ordered means that the items have a defined order, and that order will not change
# if you add new items to a list, the new items will be placed at the end of the list
# there are some list methods that will change the order, but in general : the order of the items will not change


# CHANGEABLE
# changeable means that we can change, add, and remove items in a list after it has been created

# ALLOW DUPLICATES
# as the lists are indexed, lists can have items with the same value
newlist = ['king', 'queen', 'slave', 'queen']
print(newlist)

# LIST LENGTH
# its used to determine how many items a list has, use the len() function
print(len(thisislist))
print(len(newlist))


# list items - data types
# they can be of any data type : bool, int, string
list1 = ['apple', 'banana', 'cherry', 'peanut']
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, False, True]

# a list can also contain different data types
list4 = ['abc', 34, True, 40, 'male']


# type()
# lists are defined as objects with the data type 'list'
# <class 'list'>
Newlist = ['apple', 'banana', 'cherry']
print(type(Newlist))


# THE list() CONSTRUCTOR
# it is also possible to use the list() constructor when creating a new list
NewList = list(('apple', 'banana', 'cherry'))
print(NewList)


# ACCESSING LIST ITEMS
# they are indexed and you can access them by referring to the index number
print(NewList[1])

# Negative Indexing
# it means start from the end
# -1 refers to the last item, -2 referes to the second last item
print(NewList[-1])

# range of indexes
# we can specify a range of indexes by specifying where to start and where to end the range
# when specifying a range, the return value will be a new list with the specified items
Thisislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(Thisislist[2:5]) # the start is included and the end is excluded
print(Thisislist[:4]) # no start value, it'll start from the 0th index
print(Thisislist[2:]) # no end value, it'll go till the list end


# range of negative indexes
print(Thisislist[-4:-1])

# check if item exists
# to determine if a specified item is present in a list use the in keyword
if 'apple' in Thisislist:
    print("yes, 'apple' is in the fruits list")
    



# change list items
# to change the value of a specific item, refer to the index number
Thisislist[1] = 'chocolate'
print(Thisislist)



# change a range of item values
# to change the vlauesof items within a specific range, define a list with the new values
# and refer to the range of index numbers where you want to insert the new values
Thisislist[1:3] = ['dairyMilk', 'kitkat']
print(Thisislist)

# if we insert more items than we replace, the new items will be inserted where
# you specified, and the remaining items will move accordingly
# the length of list will change when the number of items inserted does not 
# match the number of items replaced
Thisislist[1:2] = ['munch', 'perk'] # changing second value by replacing it with two new values
print(Thisislist)

# if we insert less items than we replace, the new items will be inserted where you specified, 
# and the remaining items will move accordingly
Thisislist[1:3] = ['pie']
print(Thisislist)



# INSERT ITEM
# to insert a new list item, without replacing any of the existing values, we 
# can use the insert() method
# the insert() method inserts an item at the specified index
Thisislist.insert(2, 'dark chocolate')
print(Thisislist)



# ADD LIST ITEMS
# append items : to add an item to the end of the list, use the 
# append() method
Thisislist.append('cake')
print(Thisislist)


# insert items
# to insert a list item ata specific index, use the insert() method
# the insert() method inserts an item at the specified index
Thisislist.insert(0, 'pastry')
print(Thisislist)

# extend list
# to append elements from another list to the current list, use the extend() method
flavours = ['butterscotch', 'chocolate', 'strawberry', 'belgian chocolate']
Thisislist.extend(flavours)
print(Thisislist)
flavours.extend(Thisislist)
print(flavours)


# add any iterable
# extend() method does not have to append lists, we can add any iterable object
# (tuples, sets, dictionaries)
thisistuple = ('monday', 'sunday')
flavours.extend(thisistuple)
print(flavours)





# REMOVE LIST ELEMENTS
# remove() method removes the specified item
# if there are more than one occurrence of the specified value
# remove() method removes the first occurrence
flavours.remove('sunday')
print(flavours)


# remove specified index
# pop() method removes the specified index
flavours.pop(0)
print(flavours)

# if we don't specify the index, the last item is removed
flavours.pop()
print(flavours)



# del keyword also removes the specified index
# del keyword can also delete the list completely
del flavours[3]
print(flavours)
del Thisislist


# clear the list
# clear() method empties the list
# the list still remains , but it has no content
flavours.clear()
print(flavours)




# LOOP LISTS
# we can loop through a lilst using a for loop
thisislist = ['bread', 'milk', 'eggs']
for x in thisislist:
    print(x)

# loop through the index numbers
# we can loop through the list using their index numbers
# we use range() and len() functions to create a suitable iterable
for i in range(len(thisislist)):
    print(thisislist[i])



# using a while loop
# we use a len() function to determine the length of the list, 
# then start at 0 and loop your way through the list items by referring
# to their indexes
i = 0
while i < len(thisislist):
    print(thisislist[i])
    i = i + 1 # i++ not allowed in python because , numbers are immutable


# looping using list comprehension, they are best when we build a new list
# offers the shortest syntax for looping through list
# syntax : [expression for item in iterable]
[print(x) for x in thisislist]



# LIST COMPREHENSION 
# they offer a shorter syntax when you want to create a new list based on the 
# values of an existing list

# normal way , without list comprehension
fruits = ['apple', 'mango', 'banana', 'grapes']
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)

# same thing with list comprehension
chocolates = ['perk', 'munch', 'kismi']
newchocolate = [x for x in chocolates if 'm' in x]
print(newchocolate)

# syntax : [expression for item in iterable if condition == True]
# the return value is a new list, leaving the old list unchanged

# condition : is like a filter that only accepts the items that evaluate to True

# iterable : the iterable can v=be any iterable object, like a list, tuple, set etc

# we can use range() function to create an iterable
newChocolate1 = [x for x in range(8)]
print(newChocolate1)



# expression : is the current item in the iteration , but it is also the 
# outcome, which you can manipulate it before it ends up like a list item in the new list
#set the values in the new list to upper case
newlist = [x.upper() for x in fruits]
print(newlist)

# set all values in the list to 'hello'
newlist = ['hello' for x  in fruits]
print(newlist)

# expression can also contain conditions, not like a filter, but as a way to 
# manipulate the outcome
newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist)






# SORT LIST ALPHANUMERICALLY
# list objects have a sort() method that will sort the list alphanumerically, ascending
# by default
thisislist.sort()
print(thisislist)

numberlist = [2, 4567, 89, 38, 298, 00, 2470, 987649, 2843876483]
numberlist.sort()
print(numberlist)



# sort descending
# to sort descending, use the keyword argument reverse  = True
thisislist.sort(reverse = True)
print(thisislist)

numberlist.sort(reverse = True)
print(numberlist)



# customize sort function
# for customizing our own function , we can use the
# keyword argument key = function
# the function will return a number that will be used to sort
# the list ( the lowest number first)

# eg, sort the list based on how close the number is to 50
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# case insensitive sort
# by default the sort() method is case sensitive , resulting in all 
# capital letters being sorted before lower case letters
thisislist = ['banana', 'Orange', 'Apple' , 'apple']
thisislist.sort()
print(thisislist)

# we can use a built-in function as key function when sorting a list
# for case insensitive sort , use str.lower as  akey function
thisislist.sort(key = str.lower)
print(thisislist)

# reverse order
# reverse() method reverses the current sorting order of the elements
thisislist.reverse()
print(thisislist)




# COPY LISTS
# we cannot directly copy a list simply typing list2 = list1, because:
# list2 will only be a reference to list1, and changes made in list1 will 
# automatically also be made in list2


# copy() method
thisList = ['app', 'browser', 'website']
newList = thisList.copy()
print(newList)


# another way to copy is to use built-in list() method
newlist1 = list(thisList)
print(newlist1)


# we can also make a copy of a list by using the : (slice) operator
newlist2 = thisList[:]
print(newlist2)


# JOIN LISTS
# 1. using + operator
list1 = ['a','b','c']
list2 = [1,2,3]
list3 = list1 + list2
print(list3)


# 2. appending
# another way to join two lists is by appending all the items from list2 into list1, one by one
for x in list2:
    list1.append(x)
print(list1)


# 3. extend() method
# we can use extend() method, where the purpose is to add elements from one list
# to another list
list1.extend(list2)
print(list1) # to get it's accurate answer in this file , comment out the appending method








# LIST METHODS
# 1. append() : adds an element at the end of the list
# 2. clear() : removes all the elements from the list
# 3. copy() : returns a copy of the list
# 4. count() : returns the number of elements with the specified value
# 5. extend() : add the elements of a list ( or any iterable),
#               to the end of the current list
# 6. index() : returns the index of the first element with the specified value
# 7. insert() : adds an element at the specified position
# 8. pop() : removes the element at the specified position
# 9. remove()  :removes the element at the specified value
# 10. reverse() : reverses the order of the list
# 11. sort() : sorts the list