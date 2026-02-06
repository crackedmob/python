# strings:
# they are either surrounded by single or double quotes

# Quotes Inside Quotes
# we can use quotes inside a string as long as they don't match 
# the quotes surrounding the string
print("it's alright")
print("He is called 'John'")
print('He can do "his" work')

# Assigning String to a Variable
# assigning string to a variable is done with variable name followed by an equal sign and the string:
a = "hello"
print(a)


# Multiline String
# we can assign a multiline string to a varaible by using three quotes:
# we can either use three double or single quotes 
# in the result, the line breaks are inserted at the same position as in the code.
b = """hello , i's been a while
I wanted to see you."""
print(b)


c = '''yo, i hope life has been good to you,
i don't know how to reach out to you anymore.'''
print(c)





# Strings and Arrays
# strings in python are arrays of unicode characters
# python doesn't have a character data type , a single character is 
# simply a string with a length of 1
# square brackets can be used to access elements of the string
print(a[1]) # gets you the character at popsition 1


# Looping Through a String
for x  in "banana":
    print(x)
    


# String Length
# to get the length of a string , use the len() function
# len() returns the length of a string
print(len(a))


# Check String
# to check if a certain phrase or character is present in a string, we can use keyword in
txt = "the best things in life are free"
print("free" in txt)


if "free" in txt:
    print("yes, 'free' is present.")


# Check if not
# to check if a certain phrase or character is NOT present in a string
# we can use the keyword not in
print("expensive" not in txt)


if "expensive" not in txt:
    print("No, 'expensive' is not in txt")




# Slicing Strings
# returning a range of characters by using the sloce syntax
# specify the start index and the end index, separated by a colon, to return a part of the string
d = "hello ken"
print(d[2:5]) # end is not inclusive here

# slice from the start
#[start: end]
print(d[:5])

# slice to the end
print(d[2:])

# negative indexing
# use negative indexing to statrt the slice from the end of the string:
print(d[-5: -2]) # end not included , which is -2 (from back in negative the index start from 1)




# Modify String
# upper case : upper() method return the string in upper case
e = "heLlo"
print(e.upper())


# lower case : lower() method returns the string in lower case
print(e.lower())


# Remove whitespace 
# strip() method removes any whitespace from the beginning or the end
f = "   kwen  "
print(f.strip())


# Replace string
# replace() method replaces a string with another string
print(f.replace("e", "ee"))

# Split String
# split() method returns a list where the text between the specified separator 
# becomes the list items
# spplit() method splits the string into substrings if it finds instances
# of the separator
print(d.split(" "))


# String Concatenation
# to concatenate, or combine, two strings you can use the  + operator
g = 'hi'
h = 'ken'
i = g + h # no space between them rn
print(i)

i = g + " " + h # to add space between them
print(i)



# String Format
# we cannot combine striings and numbers like the concatenation method
# but we can combine strings and numbers by usng f-strings or the format() method

# f-strings
# to specify a string as an f-string, simply put an f in front of the string
# literal, and add curly brackets {} as placeholders for variables
# and other operations.

old = 70
write = f'yoooo, i am {old}'
print(write)

# placeholder can contain variables, operations, functions, and modifiers to 
# format the value
price = 60
stat = f'the price is {price}'
print(stat)

# a placeholder cann include a modifier to format the value
# a modifier is included by adding a colon : followed by  a legal
# formatting type, like .2f which means fixed point number with 2 decimals
stat = f'the price is {price : .2f}'
print(stat)


# a placeholder can contain python code , like math operations:
stat = f'my age is {2 * 10}'
print(stat)



# Ecape Character
# to insert characters that are illegal in a string, use an escape character
# escape character is a backslash \ followed by the character you want to insert
# txt = "hello "kenny"" this is illegal , to have double quote inside double quote
txt = 'hello \'kenny\''
print(txt)