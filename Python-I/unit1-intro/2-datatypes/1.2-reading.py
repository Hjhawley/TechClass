# A data type is a classification of data that tells the computer
# how to interpret and use it. It gives context to the data.
# In Python, there are several built-in data types.

# Integers
# An integer (or int) is a whole number.
# Examples:
print(42)
print(0)
print(-17)

# Floats
# Short for 'floating point number'; a number with a decimal point.
# Examples:
print(3.14)
print(0.5)
print(-2.0)

# String
# A string is a sequence of characters enclosed in quotes.
# Examples:
print("Hello, world!")
print('Python is cool.') # Can be written with " " or ' '.
print("1234") # Even though this looks like a number, it's not.

# Boolean
# A boolean is a logical value that is either True or False.
# Examples:
print(True) # Note that this is not a string because there are no quotes.
print(False) # The word must be capitalized; Python is case-sensitive.
print(2 > 3) # This will evaluate to False, because 2 is not greater than 3.

# You can check something's data type by using the type() function.

print(type(3))
print(type(1.1))
print(type("Yellow"))
print(type(10 > 5))