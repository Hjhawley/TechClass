'''Lists
creating, indexing, slicing
append(), insert(), remove(), sort(), reverse()
List comprehension: generating lists with a simple syntax

# A string is really just an array (or list) of characters, and we can manipulate
# strings just like any other array.

# You can also use "if" statements to test for the presence of a value in a
# list or other sequence:
fruits = ['apple', 'banana', 'orange']

if 'apple' in fruits:
    print("You like apples!")
# This code will print "You like apples!" because 'apple' is in the 'fruits'
# list.
'''
# Lists

# Lists are a type of data structure in Python used to store a collection of
# items. They are ordered, mutable (can be changed), and allow for duplicate
# elements.

# Creating a list
fruits = ['apple', 'banana', 'cherry']

# Accessing items in a list
print(fruits[0]) # Output: 'apple'
print(fruits[1]) # Output: 'banana'
print(fruits[-1]) # Output: 'cherry'

# Changing an item in a list
fruits[1] = 'orange'
print(fruits) # Output: ['apple', 'orange', 'cherry']

# Looping through a list
for fruit in fruits:
    print(fruit)

# Checking if an item exists in a list
if 'apple' in fruits:
    print('Yes, apple is in the fruits list')

# Adding an item to a list
fruits.append('banana')
print(fruits) # Output: ['apple', 'orange', 'cherry', 'banana']

# Removing an item from a list
fruits.remove('cherry')
print(fruits) # Output: ['apple', 'orange', 'banana']

# Sorting a list
fruits.sort()
print(fruits) # Output: ['apple', 'banana', 'orange']

# Reversing a list
fruits.reverse()
print(fruits) # Output: ['orange', 'banana', 'apple']