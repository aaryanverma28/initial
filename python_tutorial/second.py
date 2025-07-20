print("Hello world")

"""
multi-line
comment
"""

# Arithmetic operators
a = 19
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)  # remainder
print(a ** b) # a^b

# Relational operators
a = 26
b = 20
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False

# Assignment operators
num = 10
num **= 15
print("num:", num)  # 1000000000000000

# Logical operators
a = 50
b = 60
print(not False)
print(not a > b)

val1 = False
val2 = False
print("And operator:", val1 and val2)
print("OR operator:", (a == b) or (a > b))

# Type conversion
a = int("3")
b = 5.25
print(a + b)

a = 3.15
a = str(a)
print(type(a))