# function arguments
# information can be passedinto function as arguments
# they are specified in the parenthesis of the function, we can add as many arguments as we want
# we just have to separate them with comma
def myFunc(fname): # fname is the parameter
    print(fname + ' hello')

myFunc("ken") # ken and leela are the arguments
myFunc("leela")



# parameters vs arguments
# parameter : it is the variable listed inside the parentheses in the function definition
# argument : it is the actual value that is sent to the function when it is called


# number of arguments should be same as number of parameters, if the arguments are less than parameters , we will get an error
# default parameter values can be used to avoid the error caused by arguments != parameters
# it uses the default value instead of throwing an error
def myFunc(name = "friend"):
    print("hello", name)

myFunc("ken")
myFunc()



# keyword arguments :  we can send arguments with the key = value syntax
def myFunc(animal, name):
    print("i have a", animal)
    print("my", animal + " 's name is", name)

myFunc(animal = "dog", name = "shona") # the order of the arguments doesn't matter

# the phrase keyword arguments is often shortened to kwargs 


# positional arguments
# when we call a function with arguments without using keywords, they are called positional arguments
# they must be in the correct order
def myFunc(animal, name):
    print("I have a", animal)
    print("my", animal + " 's name is", name)

myFunc("dog", "shona")




# mixing positional and keyword arguments
# here positional arguments must come before keyword arguments
def myFunc(animal, name, age):
    print("i have a ", animal, "who is", age , "years old and it's name is", name )
    print(f"i have a {animal} who is {age} years old and my {animal}'s name is {name}")

myFunc("dog", name = "shona", age = 9)




# passing different data types
def myFunc(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ['apple' ,'mango', 'cherry']
myFunc(my_fruits)


def myFunc(person):
    print('name:', person['name'])
    print('age:', person['age'])

my_person = {'name' : 'ken', 'age' : 34}
myFunc(my_person)



# return values
def myFunc(x, y):
    return x + y

result = myFunc(2, 3)
print(result)




# returning different data types
def myFunc():
    return ['apple', 'banana', 'cherry']

fruits = myFunc()
print(fruits[0])
print(fruits[1])
print(fruits[2])



def myFunc():
    return(10, 30)
x, y = myFunc()
print('x:', x)
print('y:', y)



# positional - only arguments
# we can specify that a function can have ONLY positional arguments
# to specify that , add ,/ after the arguments
def myFunc(name, /): 
    print('hello', name)

myFunc('ken')
# without ,/ we are actually allowed to use keyword arguments even if the function expects positional arguments
# keyword - only arguments
# to specify that a function can have ONLY keyword arguments, add *, before the arguments
def myFunc(*, name):
    print("hello", name)

myFunc(name = "ken")
# wothout *, we are allowed to use positional arguments even if the function expects
# keyword arguments

# combining positional -ONLY and keyword - ONLY 
# arguments before / are positional only
# and arguments after * are keyword only
def myFunc(a, b, /, *, c, d):
    return a + b + c + d
result = myFunc(5, 10, c = 15, d = 98)
print(result)