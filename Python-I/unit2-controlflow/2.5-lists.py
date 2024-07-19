# Lists

# Lists are a type of data structure in Python used to store a collection of items.
# They are ordered, mutable (able to be changed), and allow for duplicate elements.

# Creating a list:
fruits = ['apple', 'banana', 'cherry']

# Accessing items in a list:
print(fruits[0])  # Output: 'apple'. Remember that indexing starts at 0, not 1
print(fruits[1])  # Output: 'banana'
print(fruits[-1]) # Output: 'cherry'. -1 is a way to index the last item.
# -2 would be second to last, -3 third to last, etc.

# Reassigning an item in a list:
fruits[1] = 'orange'
print(fruits)  # Output: ['apple', 'orange', 'cherry']

# Looping through a list:
for fruit in fruits:
    print(fruit)

# Checking if an item exists in a list:
if 'apple' in fruits:
    print('Yes, apple is in the fruits list.')

# Adding an item to the end of a list:
fruits.append('banana')
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'banana']

# Removing an item from a list:
fruits.remove('cherry')
print(fruits)  # Output: ['apple', 'orange', 'banana']

# Sorting a list:
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'orange']

# Reversing a list:
fruits.reverse()
print(fruits)  # Output: ['orange', 'banana', 'apple']

# Slicing:
# Slicing is a way to extract a specific section of a list, string, or other
# sequence. It works by specifying the start and end index of the slice using a
# colon between them. The start index is inclusive and the end index is exclusive,
# meaning the slice includes all elements from the start index up to but not
# including the end index (just like the range() function from earlier).

# Slicing a list:
numbers = [0, 1, 2, 3, 4, 5]
slice1 = numbers[2:4] # gets [2, 3]
print(slice1)
slice2 = numbers[:3]  # gets [0, 1, 2]
print(slice2)
slice3 = numbers[3:]  # gets [3, 4, 5]
print(slice3)

# Slicing a string:
text = "Hello, world!"
slice4 = text[7:12] # gets "world"
print(slice4)

# List Comprehensions:
# List comprehensions provide a concise way to create lists.
# It consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses. The expressions can be anything,
# meaning you can put in all kinds of objects in lists.

# Creating a list of squares:
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Creating a list of even numbers:
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# List comprehensions can also include complex expressions and nested functions:
combinations = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combinations)  # Output: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
