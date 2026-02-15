# DICTIONARIES
thisisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisisdict)
# they are used to store data values in key : value pairs
# it is a collection which is ordered, changeable and do not allow duplicates
# they are written with curly brackets, and have keys and values
# dictionary items can be referred to by usinng the key name
print(thisisdict["brand"])


# ordered : means the dictionary have a defined order, and that will not change
# unordered : means that the items do not have a defined order, you cannot refer to an item by using an index
# changeable : means that we can change, add or remove items after the dictionary has been changed
# duplicates not allowed : and due to that the dictionary cannot have two items with the same key
thisisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2026
} # if we add one more year with the year key
# the later one will be printed if we will print the dictionary , basically it will overwrite
print(thisisdict)




# dictionary length
print(len(thisisdict))
# the dictionary items can be of any data type

# type() prints the type of data type used
print(type(thisisdict))




# dict() constructor
# we can use the constructor to make a dictionary
thisisdict = dict(name = "John" , age = 34, country = "India")
print(thisisdict)




# ACCESS DICTIONARY ITEMS
thisisdict = {
    "brand" : "Ford",
    "Model" : "Mustang",
    "year" : 2926
}
x = thisisdict["Model"]
print(x)
# get() method will give us the dsame result
x = thisisdict.get("Model")
print(x)


# get keys, keys() method will return a list of all the keys in the dictionary
print(thisisdict.keys())
# The list of the keys is a view of the dictionary, meaning that any 
# changes done to the dictionary will be reflected in the keys list.

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 3039
}
x = car.keys()
print(x)

car['color'] = 'white'
print(x)


# get values, values() method will return a list of all the values in the dictionary
x = thisisdict.values()
print(x)
# The list of the values is a view of the dictionary, meaning that any changes done to 
# the dictionary will be reflected in the values list.
car['year'] = 2023
x = car.values()
print(x)


# get items, items() method return each item ina dictionary, as tuples in a list
x = thisisdict.items()
print(x)

x = car.items()
print(x)

car['year'] = 2040
print(x)



# check if key exists
# to determine that if a specified key ecxists or is present in a ditionary 
# we use the in keyword
if "model" in car:
    print("yes")


# CHANGE DICTIONARY ITEMS
# we can change a specific item by referring to it's key name
thisdict = {
    "game" : "basketball",
    "state" : "rajasthan",
    "age_group" : 18
}
thisdict["age_group"] = 14
print(thisdict)

# update dictionary
# update() method will update the dictionary with the items from the given argument
# the argument must be a dictionary , or an iterable with key : value pairs
thisdict.update({'state' : 'delhi'})
print(thisdict)


# ADD DICTIONARY ITEMS
# done by using a new index key and assigning a value to it
thisdict["category"] = "male"
print(thisdict)

# update dictionary
# update() method will update the dictionary with the items from a given 
# argument. if the item does not exist, the item will be added
thisdict.update({'category' : 'female'})
print(thisdict)



# REMOVE DICTIONARY ITEMS
# pop() removes the item with the specified key name
thisdict.pop('category')
print(thisdict)

# popitem() removes the last inserted item
thisdict.popitem()
print(thisdict)


# del keyword removes the item with the specified key name
del thisdict['state']
print(thisdict)
# del can also delete the dictionary completely
del thisdict
#print(thisdict) # this will cause an error as thisdict no longer exists


# clear() empties the dictionary
car.clear()
print(car)



# LOOP DICTIONARIES
# the return value are the keys of the dictionary, but there are methods to return the values as well
for x  in thisisdict:
    print(x)


# this prints the values
for x in thisisdict:
    print(thisisdict[x])


# value() to return the values of dictionary
for x  in thisisdict.values():
    print(x)


# we can use keys() to return the keys of a dictionary
for x in thisisdict.keys():
    print(x)


# loop through both keys and values, by using the items() method
for x, y in thisisdict.items():
    print(x,y)




# COPY DICTIONARY
# you can't copy a dictionary simply by doing dict1 = dict2
# it will just be a reference to dict1, and changes made to dict1 will automatically also be made in dict2
mydict = thisisdict.copy()
print(mydict)


# dict() built-in function
mydict = dict(thisisdict)
print(mydict)



# NESTED DICTIONARIES
# a dictionary containing dictionary is called nested dictionary
myfamily = {  # a dictionary that contain three dictionaries
    "child1" : {
        'name' : 'ken',
        'year' : 2004
    },
    "child2" : {
        'name' : 'yam',
        'year' : 2005
    },
    "child3" : {
        'name' : 'Pam',
        'year' : 2006
    }
}



# add three dictionaries to a dictionary
child1 = {
    'name' : 'ken',
    'year' : 2004
}
child2 = {
    'name' : 'yen',
    'year' : 2004
}
child3 = {
    'name' : 'pen',
    'year' : 2004
}
myfamily = {
    'child1' : child1,
    'child2' : child2,
    'child3' : child3
}
print(myfamily)



# access items in nested dictionaries
# we use the name of the dictionaries, starting with the outer dictionary
print(myfamily["child1"]["year"])



# loop through nested dictionaries
# items() gives the key and values together
for x, obj in myfamily.items(): # it loops and prints each inner dictionary , more like loops and prints each family member name
# for person_name, person_details in myfamily.items():   
    print(x)

    for y in obj: # now here it loops and prints each family members details
        print(y + ':', obj[y]) 
        # print(detail, ':', person_details[detail])



