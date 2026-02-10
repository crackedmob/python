# *args and **kwargs
# by default a function must be called with the correct number of arguments
# though, sometimes we may not know how many arguments will be passed into our function
# *args and **kwargs allow functions to accept a unknown number of arguments


# Arbitrary Arguments - *args
# if we do not know how many arguments will be passed into our function
# add a * before the parameter name
# this way a function will receive a tuple of arguments and can access the items accordingly
def myFunc(*kids):
    print("the older one is " + kids[0])

myFunc('kenny', 'benny', 'nanny')

# *args parameter allows a function to accept any number of positional arguments
# inside the function, args becomes a tuple containing all the passed arguments
# accessing individual arguments from *args
def myFunc(*args):
    print("type:" , type(args))
    print('1st argument:', args[0])
    print('2nd argument:', args[1])
    print('all arguments:', args)

myFunc('ken', 'pen', 'van')




# using *args as regular arguments
# we can combine regular parameter with *args
# regular parameter must come before *args
def myFunc(greeting, *names):
    for name in names :
        print(greeting, name)

myFunc("hello", 'ken', 'van', 'lan')





def myCalc(*numbers):
    total = 0
    for num in numbers :
        total += num
    return total

print(myCalc(1, 2, 3))
print(myCalc(34, 56, 0))


# Arbtrary Keyword Rguments - **kwargs
# when we do not know how many keyword arguments will be passed into our function, 
# add two asterisks ** before the parameter name
def myFunc(**kid):
    print('his last name is ' + kid['lname'])

myFunc(fnam = 'ken', lname = 'kaneki')


# **kwargs allows a function to accept any u=number of keyword arguments
# inside a function , kwargs becimes a dictionary containing all the keyword arguments
def myFunc(**myVar):
    print('type:', type(myVar))
    print('name:', myVar['name'])
    print('age:', myVar['age'])
    print('all data:', myVar)

myFunc(name = 'kenny', age = 4, city = 'ajmer')


# using **kwargs with regular arguments
# regular parameters must come before **kwargs
def myFunc(username, **details):
    print('username:', username)
    print('additional details:')
    for key, value in details.items():
        print(" ", key + ":", value)

myFunc('kennyPookie', age = 45,  city = 'berlin', hobby = 'bed rotting')



# combining *args and **kwargs
# the order must be:
# 1. regular parameters
# 2. *args
# 3. **kwargs
def myFunc(title, *args, **kwargs):
    print('title:', title)
    print('positional arguments:', args)
    print('keyword arguments:', kwargs)

myFunc('user info', 'kenny', 'louis', age = 45, city = 'berlin')



# unpacking arguments
# * and ** operator can also be used when calling functions to unpack(expand) a list or dictionary into separate arguments
# unoacking lists with *
def myFunc(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = myFunc(*numbers)
print(result)


# unpacking dictionaries with **
def myFunc(fname, lname):
    print("hello", fname, lname)

person = {'fname' : 'kenny', 'lname' : 'pookie'}
myFunc(**person)