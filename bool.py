# Python Boolean
# boolean represent one of the two values : True or False
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if a > b:
    print('b is greater than a')
else:
    print('a is greater than b')
    

# Evaluate values and variables
# bool() function allows you to evaluate any value and give you true or false in return
print(bool('hello'))
print(bool(15))

x = 'hi'
y = 46
print(bool(x))
print(bool(y))

# almost all the values are evaluated to true if they have any content 
# any string is true except the empty string
# any number is true except the number 0
# any list, tuple, set, and dictionary are true , except the empty ones


# a value or object , evaluates to false , if the object is made from a 
# class with a  __len__ function that returns 0 or false
class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))




# functions can return a boolean
def myFunction():
    return True

print(myFunction())



# we can execute code based on the boolean answer of a function:
def myFun():
    return True

if myFun():
    print("Yes")
else:
    print("No")


# isinstance() is a function , which is used to determine if an object is of certain data type
# it returns a boolean value
z = 909
print(isinstance(z, int))
