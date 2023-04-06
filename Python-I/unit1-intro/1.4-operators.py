# Operators

# Operators are symbols and keywords that allow you to perform operations on
# values or variables.

# 1. Arithmetic Operators
# Arithmetic operators are used to perform mathematical operations on values.
# Examples:
x = 10
y = 3
print(x + y) # Addition: Adds the values of x and y.
print(x - y) # Subtraction: Subtracts the value of y from x.
print(x * y) # Multiplication: Multiplies the values of x and y.
print(x / y) # Division: Divides the value of x by y.
print(x % y) # Modulo: Returns the remainder of x divided by y.
print(x ** y) # Exponentiation: Raises x to the power of y.

# 2. Comparison Operators
# Comparison operators are used to compare values and return a Boolean value.
# Also called 'relational operators'.
# Examples:
x = 5
y = 10
print(x == y) # Equal to: Returns True if x is equal to y, otherwise False. Not to be confused with =.
print(x != y) # Not equal to: Returns True if x is not equal to y, otherwise False.
print(x > y) # Greater than: Returns True if x is greater than y, otherwise False.
print(x < y) # Less than: Returns True if x is less than y, otherwise False.
print(x >= y) # Greater than or equal to: Returns True if x is greater than or equal to y, otherwise False.
print(x <= y) # Less than or equal to: Returns True if x is less than or equal to y, otherwise False.
# When comparing strings, Python compares the characters' ASCII values.
# Essentially this means alphabetical order, with earlier letters being "smaller".
print("Apple" < "Zebra") # This will return True.

# 3. Logical Operators
# Logical operators are used to combine multiple conditions and return a
# Boolean value.
# Examples:
x = 5
y = 10
z = 15
# And operator: Returns True if both conditions are True.
print(x < y and y < z) # Should return True
# Or operator: Returns True if at least one condition is True.
print(x > y or y < z) # Should return True
# Not operator: Inverts the result of a condition.
print(not x > y) # Should return True

# 4. Assignment Operators
# Assignment operators are used to assign values to variables.
# Examples:
x = 5 # Basic assignment operator. Be careful not to confuse with == which is completely different.
# There are also "incremental operators" which combine arithmetic with assignment.
x += 3 # Add AND: Same as x = x + 3
x -= 2 # Subtract AND: Same as x = x - 2
x *= 4 # Multiply AND: Same as x = x * 4
x /= 2 # Divide AND: Same as x = x / 2
x %= 3 # Modulus AND: Same as x = x % 3
x **= 2 # Exponent AND: Same as x = x ** 2
x //= 3 # Floor Division AND: Same as x = x // 3
# You should know that the order of operations in Python follows the standard math
# conventions, with multiplication and division happening before addition and subtraction.
# Parentheses can be used to override the order of operations.