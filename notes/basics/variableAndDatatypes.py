# dealing with information and data requires us to store them , and for that we use variables
# variables are xtremely helpful to store the data or values
character_name = "John" # variable for characters name
character_age = "35" # variable for the character's age
print("There once was a man named " + character_name + " , ")
print("he was " + character_age + " years old. ")
character_name = "ken"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")
 # without variables , if i have to change the name or the age , i'll have to do that manually at every space , which
 # is tiresome and not feasible if there are a lot of statements
 # using variables we can do it at once.
 # using variables we can modify the story

# variables are containers for storing data values
# pyhton has no command for declaring a variable
x = 5
y = "Hello, World!"
# a variable is created the moment you first assign a value
# variables do not need to be declared with any particular type, and can even change type after 
# they have been set.
x = "Sally"
print(x)





# casting: 
# if you want to specify the data type of a variable , this can be done with 
# casting
x = str(3) # x will be '3
y = int(3) # y will be 3
z = float(3) # z will be 3.0




# Get the type 
# to get the type of the varable we use type() function
x = 5
y = "John"
print(type(x))
print(type(y))


# variable names are case - sensitive
a = 4
A = "pi"
# this will create two different variables




# Variable names
# - must start with a letter or the underscore character
# - variable cannot start with a number
# - it can onlt contain alpha-numeric characters and underscore
# - variable names are case-sensitive
# - variable name cannot be of any python keywords




# Assign multiple values
x, y, z = 'Orange', 'Banana', 'Cherry' # the number of variables should match the numbmer of values
print(x)
print(y)
print(z)



# one value to multiple variabes is also possible
a = b = c = 'Kween'
print(a)
print(b)
print(c)

# Unpack a collection
# if you have a collection of values in a list, tuple etc. Python 
# allows you to extract the values into variables. this is called unpacking 

# - unpack a list
fruits = ['apple' , 'banana', 'watermelon']
d, e, f = fruits
print(d)
print(e)
print(f)



# output variables
# print() function is often used to output variables
x = "Python is awesome"
print(x)

# we can output variables, separated by comma:
x = "Python "
y = 'is '
z = 'awesome'
print(x, y, z)


# instread of comma we can also use the + operator to output
# multiple variables:
print(x + y + z) # we need to have space character after x and y , otherwise the output will be Pythonisawesome


#  + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

z = "ken"
# print(x + z) will give an error as both of them are of different data type
# to print multiple variable of different data type we use comma to separate them 
print(x, z)




# Global variables 
# the variables which are created outside of a function are known as 
# global variables.
# they can be used by everyone, both inside or outside of function

x = 'awesome'

def muFunc():
    print("python is " + x)
    
muFunc()


# if we create a variable with the same name inside the function , it will be 
# local variable, and can only be used inside the function 

x = 'awesome'

def myFunc():
    x = 'crazy'
    print('python is ' + x)

myFunc()

print('python is ' + x)


# normally when we create a variable inside a function it is treated as a
# local variable , to make it global , we have to use 'global' keyword 
# it will make the variable belog to the global scope
def myFun():
    global x
    x = 'chill'

myFun()

print("python is so " + x)


# we can also use global keyword if we want to change it inside a function
x = 'awesome'

def MyFun():
    global x
    x = 'cool'

MyFun()
print('python is ' + x)






# Built-in datatypes
# variables can store data of different types, and different types can do different things
# text type: str
# Numeric types: int, float, complex
# Sequence types: list, tuple, range
# Mapping type: dict
# Set types: set, frozenset
# Boolean type: bool
# Binary types: bytes, bbytesarray, memoryview
# None type: NoneType

# declaring the data type
x = 'hi'
x = 20 # int
x = 20.5 # float
x = 1j # complex
x = ['apple', 'kween', 'hi'] # list
x = ('hi' , 'bye', 'yo') # tuple
x = range(6) # range type , displays content from 0 to n-1
x = {'name' : 'john', 'age': '34'} # dict
x = {'apple', 'banana', 'cherry'} #set
x = frozenset({'apple', 'banana', 'cherry'}) # frozenset
x = True # boolean
x = b"Hello" # bytes
x = bytearray(5) # bytearray, creates an array of size 5
x = memoryview(bytes(5)) # memoryview
x = None # NoneType



# setting the specific datatype
x = str('hi')
x = int(20) # int
x = float(20.5) # float
x = complex(1j) # complex, j is the imaginary part
x = list(('apple', 'kween', 'hi')) # list
x = tuple(('hi' , 'bye', 'yo')) # tuple
x = range(6) # range type , displays content from 0 to n-1
x = dict(name = 'john', age = '34') # dict
x = set(('apple', 'banana', 'cherry')) #set
x = frozenset(('apple', 'banana', 'cherry')) # frozenset
x = bool(5) # boolean
x = b"Hello" # bytes
x = bytearray(5) # bytearray, creates an array of size 5
x = memoryview(bytes(5)) # memoryview
x = None # NoneType





# type conversion is converting a variable from one type to another 
# int() , float(), complex() methods are used 
x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)
