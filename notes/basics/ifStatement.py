# IF STATEMENT
# equals : a == b
# not equals : a != b
# less than : a < b
# less than or equal to : a <= b
# greater than : a > b
# greater than or equal to : a >= b

a = 88
b = 24
if a > b:
    print("'b' is smaller")




if a == b:
    print("both are equal")
else:
    print("not equal")



age = 20
if age >= 18:
    print("you are an adult")
    print("you can vote")
    print("you have full legal rights")



# using variables in conditions
is_logged_in = True
if is_logged_in:
    print("hello")


# zero, empty strings(""), none, and empty collections are treated as False
# everything else is treated as True


# ELIF STATEMENTS
# elif keyword allows us to check multiple expressions for True and execute
# a block of code as soon as one of the conditions evaluate to True
a = 40
b = 89
if b < a:
    print("'a' is bigger")
elif a == b:
    print('both are equal')
else:
    print("'b' is bigger")



# ELSE STATEMENT
# else is executed when if and elif evaluate to False


# ELSE AS FALLBACK
# else is executed when none of the other blocks satisfy the condition
# this makes it useful for the error handling, validation, and providing default values

username = 'Emil'

if len(username) > 0:
    print(f"welcome, {username}")
else:
    print("error: username can't be empty")


a = 8
b = 6
if a > b : print("a is greater")

# one line if-else
print("A") if a > b else print("B")

print("A") if a > b else print("=") if a == b else print("B")



# LOGICAL OPERATORS
# and : returns true if both the conditions are true
# or : returns true if one of the condition is true
# not : reverses the result, returns false if the result is true
a = 200
b = 33
c = 500
if a > b and c > a:
    print("c is the maax element")


if a > b or b > c:
    print("one condition is true")


if not a < b:
    print("a is greater")



age = 25
is_student = False
has_coupon = True

if(age < 18 or age > 65) and not is_student or has_coupon :
    print('discount applies')





# PASS STATEMENT
# if statement cannot be empty, but if we for some reason have an if
# statement empty with no content, put in the pass statement to avoid getting an error

a = 20
b = 300
if b > a:
    pass # it is a null operation - nothing happens when it executes. 
         # it serves as a placeholder