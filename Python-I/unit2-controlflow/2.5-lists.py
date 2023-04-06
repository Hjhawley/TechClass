# Data Structures

# A data structure is a way of organizing and storing data in a program so that it
# can be accessed and used efficiently. It refers to a collection of data elements
# and the relationships among them, along with the functions or operations that can
# be applied to the data. There are many types, such as arrays (called "lists" in
# Python) and maps (called "dictionaries" in Python).

# Lists

# Lists are a type of data structure in Python used to store a collection of items.
# They are ordered, mutable (able to be changed), and allow for duplicate elements.

# Creating a list:
fruits = ['apple', 'banana', 'cherry']

# Accessing items in a list:
print(fruits[0]) # Output: 'apple'. Remember that indexing starts at 0, not 1
print(fruits[1]) # Output: 'banana'.
print(fruits[-1]) # Output: 'cherry'. -1 is a way to index the last item.
# -2 would be second to last, -3 third to last, etc.

# Reassigning an item in a list:
fruits[1] = 'orange'
print(fruits) # Output: ['apple', 'orange', 'cherry']

# Looping through a list:
for fruit in fruits:
    print(fruit)

# Checking if an item exists in a list:
if 'apple' in fruits:
    print('Yes, apple is in the fruits list.')

# Adding an item to the end of a list:
fruits.append('banana')
print(fruits) # Output: ['apple', 'orange', 'cherry', 'banana']

# Removing an item from a list:
fruits.remove('cherry')
print(fruits) # Output: ['apple', 'orange', 'banana']

# Sorting a list:
fruits.sort()
print(fruits) # Output: ['apple', 'banana', 'orange']

# Reversing a list:
fruits.reverse()
print(fruits) # Output: ['orange', 'banana', 'apple']

# Slicing
# Slicing is a way to extract a specific section of a list, string, or other
# sequence. It works by specifying the start and end index of the slice using a
# colon between them. The start index is inclusive and the end index is exclusive,
# meaning the slice includes all elements from the start index up to but not
# including the end index (just like the range() function from earlier).

# Slicing a list
numbers = [0, 1, 2, 3, 4, 5]
slice1 = numbers[2:4] # gets [2, 3]
print(slice1)
slice2 = numbers[:3] # gets [0, 1, 2]
print(slice2)
slice3 = numbers[3:] # gets [3, 4, 5]
print(slice3)

# Slicing a string
text = "Hello, world!"
slice4 = text[7:12] # gets "world"
print(slice4)