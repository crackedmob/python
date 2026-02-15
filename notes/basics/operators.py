# operators:
# they are used to perform operations on variables and values
print(10 + 5) # used for addition 

# the + operator is used to add two values, but it can also be used to add
# a variable and a value, or two variables together
sum1 = 100 + 50
sum2 = sum1 + 240
sum3 = sum2 + sum2
print(sum1)
print(sum2)
print(sum3)


# python divides the operators in various groups like any other language
# 1. arithmetic operators
# 2. assignment operators
# 3. comparison operators
# 4. logical operators
# 5. identity operators
# 6. membership operators
# 7. bitwise operators



# 1. ARITHMETIC OPERATORS
# they are used with numeric values to perform common mathematical operations
x = 15
y = 4
print(x + y) # addition
print(x - y) # subtraction
print(x * y) # multiplication
print(x / y) # division, this returns a float value or a float result
print(x % y) # modulus, return the remainder
print(x ** y) # exponentiation
print(x // y) # floor division, return the integer division, round downs to nearest whole value



# 2. ASSIGNMENT OPERATORS
# they are used to assign values to variables
# x = 5
# += , x += 3, x = x +3
# -=, x -= 3, x = x - 3
# *=, x *= 3, x = x * 3
# /=, x /= 3, x = x / 3
# %=, x %= 3, x = x % 3
# //=, x //= 3, x = x // 3
# **=, x **= 3, x = x ** 3
# &=, x &= 3, x = x & 3, bitwise AND operator, keeps only if both are 1
# |= , x |= 3, x = x | 3, bitwise OR operator, keeps if either is 1
# ^=, x ^= 3, x = x ^ 3, bitwise XOR operator, if different bits->1, same bits->0
# >>=, x >>= 3, x = x >> 3, right shift, moves bits to the right , dropping bits from the right, each right shift divides by 2
# <<=, x <<= 3, x = x << 3, left shift, moves bits to the left, adding zeros on the right, multiply by 2 at each shift
# :=, print(x := 3), x =3 print(x), this is the walrus operator
# it assigns values to variables as part of a larger expression

numbers = [1, 2, 3, 4, 5]

if(count := len(numbers)) > 3:
    print(f'List has {count} elements')



# 3. COMPARISON OPERATORS
# they are used to compare two values
# they return true or false based on the comparison
a = 3
b = 4
print(a == b) # equal operator
print(a != b) # no equal operator
print(a > b) # greater than operator
print(a < b) # less than operator
print(a >= b) # greater than or equal to 
print(a <= b) # less than or equal to

# chaining comparison operators
print(1 < a < 10)
print(a < 2 and b > 10)



# 4. LOGICAL OPERATORS
# they are used to combine conditional statements
# 1. and : returns true if both the sdtatements are true
# 2. or : returns true if one of the statements is true
# 3. not : reverse the result, returns false if the result is true and vice versa
print(a > 0 and a < 10)
print(a < 2 or a == 0)
print(not(a > 3 and a < 10))



# 5. IDENTITY OPERATORS
# they are used to compare objects, not if they are equal , but if they are 
# actually the same objects, with the same memory location
# 1. is : returns true if both variables are the same object
# 2. is not : returns true if both variables are not the same object
c = ['apple', 'banana']
d = ['apple', 'banana']
e = c

print(c is e)
print(c == d)
print(d == e)


print(c is not d)
# is  : checks if both variables point to the same object in memory
# == : checks if the values of both variables are equal



# 6. MEMBERSHIP OPERATORS
# they are used to test if a sequence is presented in an object
# 1. in : returns tre if a sequence with the specified value is present in the object
# 2. not in : returns true if a sequence  with the specified value is not present in the object
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)
print('pineapple' not in fruits)

# they also work in strings
text = 'hello world'
print('H' in text)
print('hello' in text)
print('D' not in text)


# 7. BITWISE OPERATORS
# they are used to compare (binary) numbers
# & : AND, sets each bit to 1 if both bits are 1 , x & y
# | : OR, sets each bit to 1 if one of two bits is 1, x | y
# ^ : XOR, sets each bit to 1 if only one of two bits is 1, x ^ y
# ~ : NOT, inverts all the bits , ~x
# << : zero fill left shift, shift left by pushing zeros in from the right and let the leftmost bits fall off, x << 2
# >> : signed right shift, shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# 6 & 3 ->  6 : 0110, 3 : 0011 , answer will be  = 0010 : 2 in decimal
# 6 | 3 -> 6 : 0110, 3 : 0011 , answer will be = 0111 : 7 in decimal
# 6 ^ 3 -> 6 : 0110, 3 : 0011, answer will be = 0101 : 5 in decimal 



# 8. OPERATOR PRECEDENCE
# they describes the order in which operations are performed
# 1. (), parentheses
# 2. ** , exponentiation
# 3. +x -x ~x , unary plus, unary minus, and bitwise NOT
# 4. * / // %, multiplication, division, floor division, and modulus
# 5. + - , addition and subtraction
# 6. << >> , bitwise left and right shifts
# 7. &, Bitwise AND
# 8. ^, bitwise XOR
# 9. |, bitwise OR
# 10. == != > >= < <= is, is not, in , not in , comparison , identity, and membership operators
# 11. not , logical NOT
# 12. and, AND
# 13. or, OR
# if two operators are of the same precedence, the expression is evaluated from left to right
