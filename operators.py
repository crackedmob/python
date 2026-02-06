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
# :=, print(x := 3), x =3 print(x)