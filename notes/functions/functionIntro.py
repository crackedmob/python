# functions : is a block of code which only runs when it is called
# it can return a data as a result
# it helps avoiding repetition
# def keyword is used to create a function
def my_func():
    print("hello")

# calling a function
my_func()
# we can call the same function multiple times
my_func()
my_func()

# function names are case sensitive, it must start with a letter or underscore
# it can only contain letters, numbers, and underscores

temp1 = 77
def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9

print(fahrenheit_to_celsius(88))


