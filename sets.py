# SETS
# sets are written with curly brackets
myset = {'apple', 'mango', 'banana'}
# sets are used to store multiple items in a single variable
# a set is a collection which is unordered, unchangeable*, and unindexed

# set items are unchangeable, but you can remove and add new items
thisisset = {'sunflower', 'tulip', 'rose'}
print(thisisset)
# as sets are unordered, we cannot be sure in which order the items will appear
# set items are unordered, unchangeable, and do not allow duplicate values

# unordered
# means that the items in a set do not have a defined order
# they can appear in a different order everytime we use them, and cannot be 
# referred to by index or key

# unchangeable
# means that we cannot change the items after the set has been created
# once a set is created , we cannot change its items, but we can remove or add
# new items


# duplicates not allowed
# sets cannot have two items with same value
thisisset = {'apple', 'banana', 'banana'}
print(thisisset) # during print only the unique values will be printed

# the values True and 1 are considered the same value in sets,
# and are treated as duplicates.
set1 = {False, True, 1, 2}
print(set1)
# the values False and 0 are considered the same in sets, 
# and are treated as duplicates
set1 = {False, 0, 2, True}
print(set1)



# get the length of a set
# to get the length and determine how many items a set has, we use
# len() function
print(len(thisisset))

# data types
# set items can be of any data type :string, int and boolean
set1 = {'apple', 'mango', 'cherry'}
set2 = {1, 2, 3, 4}
set3 = {True, False, False}

# a set can contain different data types too
set4 = {False, 1, 'hello'}


# type() : sets are defined as objects with the data type 'set'
# <class 'set'>
print(type(set1))
print(type(set2))
print(type(set3))
print(type(set4))


# set() constructor
# it is also ossible to use set() constructor to make a set
thisisset = set(('apple', 'mango', 'banana'))
print(thisisset)




# ACCESS SET ITEMS
# we cannot access items in a set by referring to an index or a key
# but we can loop through the set using a for loop, or ask if a 
# specified value is present in a set, by using the in keyword
thisisset = {'apple', 'mango', 'banana'}
for x in thisisset:
    print(x)


# check if banana is present in the set
print('banana' in thisisset)

# check if banana is not present in the set
print('banana' not in thisisset)


# once a set is created , we cannot change its items, but we can add new ones


# ADD SET ITEMS
# to add one item to a set we use add() method
thisisset = {'apple', 'mango', 'cherry'}
thisisset.add('orange')
print(thisisset)



# to add items from another set into the current set, we use update() method
thisisset = {'apple', 'mango', 'cherry'}
tropical = {'papaya', 'pineapple'}

thisisset.update(tropical)
print(thisisset)



# add nay iterable
# the object in the update() method does not have to be a set, it cann be 
# any iterable object
thisisset = {'apple', 'mango', 'cherry'}
mylist = ['kiwi', 'orange']

thisisset.update(mylist)
print(thisisset)

# REMOVE SET ITEMS
# to remove an item in a set, we use remove(), or discard() method
thisisset = {'banana', 'apple', 'mango'}
thisisset.remove('banana') # if the item to be removed does not exist, remove() will raise an error
print(thisisset)


thisisset.discard('apple') # if the item to remove does not exist, discard() will not raise an error
print(thisisset)

# we can also use the pop() method to remove an item, but this method will remove
# a random item, so you cannot be sure what item that gets removed
# the return value of the pop() method is the removed item
thisisset = {'apple', 'mango', 'pineapple'}
x = thisisset.pop()
print(x)
print(thisisset)



# the clear() method empties the set
thisisset.clear()
print(thisisset)


# del keyword will delete the set completely
#thisisset = {'apple', 'mango', 'cherry'}
#del thisisset
#print(thisisset) # this will raise an error as the set no longer exists




# LOOP SETS
thisisset = {'apple', 'mango', 'cherry'}
for x in thisisset:
    print(x)




# JOIN SETS
# union() and update() methods joins all items from both sets
# intersection() method keeps ONLY the duplicates
# difference() method keeps the items from the first set that are not 
# in the other set(s)
# symmetric_difference() method keeps all the items EXCEPT the duplicates


# 1. union() method returns a new set with all items from both sets
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# we can use | operator instead of the union() method, and you will get the same result
set3 = set1 | set2
print(set3)

# join multiple sets
# when using a method, just add more sets in the parentheses, separated by commas

myset = set1.union(set2, set3)
print(myset)

# we can use the | operator
myset = set1 | set2 | set3
print(myset)

# join a set and a tuple
# union() method allows us to join a set with other data type
# the result will be set
x = {'a', 'b', 'c'}
y = (1, 2, 4)

z = x.union(y)
print(z)
# the  | operator only allows us to join set with set, nd not with 
# other data types like you can write with union() method

# update
# update() method inserts all items from one set into another
# update() method changes the original set, and does not return a new set

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
# both union() and update() will exclude any duplpicate items

# intersection
# keep ONLY the duplicates
# intersection() method will return a new set, that only contains
# the items that are present in both sets

set1 = {'apple', 'mango', 'cherry'}
set2 = {'banana', 'cherry', 'grapes'}

set3 = set1.intersection(set2)
print(set3)
# we can use & operator instead of intersection() method, and we will
# get the same result
set3 = set1 & set2
print(set3)
# & operator only allows us to join sets with sets , and not with other data types
# like you can with the intersection() method


# intersection_update() method will also keep ONLY the duplicates, but 
# it will change the original set instead of returing a new set
set1.intersection_update(set2)
print(set1)



# difference
# difference() method will return a new set that will contain only the items from the 
# first set that are not present in the second set
set1 = {'app', 'game', 'web'}
set2 = {'babe', 'web', 'tab'}

set3 = set1.difference(set2)
print(set3)

# we can use  - operator instead of the difference() method, and we will get the same result
set3 = set1 - set2
print(set3)
# the - operator only allows us to join sets with sets, 
# and not with other data types like we can with the difference() method

# the difference_update() method does what difference() method does, but 
# instead oof making another new set for the answer. 
# it updates the original one
set1.difference_update(set2)
print(set1)



# symmetric differences
# symmetric_difference() method will keep only the elements that are NOT
# present in both sets
# basically removes the common and union the left of the elements
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 4, 'a'}
set3 = set1.symmetric_difference(set2)
print(set3)

# ^ operator does the same work as the symmetric_difference() method
set3 = set1 ^ set2
print(set3)
# ^ operator only allows us to join the sets with sets, and not other data types
# symmetric_difference() method allows us to perform with others too


# symmetric_difference_update() method will do the same thing but it will change the 
# original set instead of returning a new set
set1.symmetric_difference_update(set2)
print(set1)




# frozenset
# it is an immutable version of set
# it contains unique, unordered, unchangeable elements
# here elements cannot be added or removed from a frozenset
# it supports all non-mutating operations ofsets


# creating a frozenset
frozenset() # this is a constructor which is used to create a frozenset
# from any iterable
x = frozenset({'a', 'b', 'v'})
print(x)
print(type(x))


# frozenset methods
# 1. copy() : returns a shallow copy

# SHALLOW COPY : i can make a new set, but the things/items inside it are still shared
# it creates a new outer object
# inner objects are shared
# changes made to inner objects affect both
# e.g., a = [[1, 2], [3, 4]]
# b = a.copy() -> shallow copy created
# now, a is[[1, 2], [3, 4]]
# b is [[1, 2], [3, 4]]
# now we perform b[0].append(99)
# a becomes [[1, 2, 99], [3, 4]]
# b becomes [[1, 2, 99], [3, 4]]
# a changed when we changed b , because the items inside them are the same thing
# just the containers are different

# DEEP COPY
# here we make a new aet and make new copies of everything inside it 
# nothing is shared
# e.g., import copy
# a = [[1,2],[3,4]]
# b = copy.deepcopy(a) -> b is completely independent
# b[0].append(99)
# a is [[1,2],[3,4]]
# b is [[1,2,99],[3,4]]
# creating a deep copy:
# import copy
# new_list = copy.deepcopy(old_list)

# 2. difference() , - : returns a new frozenset with the difference
# 3. intersection(), & : returns a new frozenset with the intersection
# 4. isdisjoint() : returns whether two frozenset have an intersection
# 5. isisubset(), <=/ < : returns true if this frozendset is a (proper) subset of another
# 6. issuperset(), >=/ > : returns true if this frozenset is a (proper) superset of another
# 7. symmetric_difference() , ^ : returns a new frozenset with the symmetric differences
# 8. union(), | : returns a new frozenset contining the union