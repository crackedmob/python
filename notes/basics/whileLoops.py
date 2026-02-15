# WHILE LOOPS
# while loops 
# for loops 
# these are the only two loops in python

# while loop executes a set of statements as long as the condition is true
i = 1
while i < 6: # while loop requires relevant variab;e to be ready
    print(i)
    i += 1

# break statement can stop the loop even if the while condition is true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1



# continue statement can stop the current iteraton, and continue with the next
i = 0
while i < 6:
    i += 1
    if i == 4:
        continue
    print(i)



i = 1
while i < 6:
    print(i)
    i += 1
else: # will not be executed if the bloack is stopped by a break statement
    print("i > 6 now")


# FOR LOOPS
# it's used for iterating over a sequence
# for does not require an indexing variable set beforehand
fruits = ['apple', 'mango', 'grapes']
for x  in fruits:
    print(x)


for x in "banana":
    print(x)



# break in for loop
for x in fruits:
    print(x)
    if x == 'mango':
        break # it gets printed up until mango and then stops



for x in fruits:
    if x == 'mango':
        break
    print(x) # here only apple will be printed because the print statement is after break and the loop break as soon as the mango is identified




for x  in fruits:
    if x == 'apple':
        continue
    print(x)



# range() function
# loop trhough a set of code a specified number of times
# it returns a sequence of numbers, starting from 0 by default,
# andd increment by 1(by default) , and ends at a specified number

for x  in range(6): # 0 - 5 
    print(x)

# range(start, end, increment) this is also possible but end value is not included

# nested loops
# a loop inside another loop is a nested loop
# inner loop gets executed for each iteration of the outer loop
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']

for x  in adj:
    for y in fruits:
        print(x, y)