# Dictionaries

# Dictionaries are a type of data structure that store a collection of key-value pairs.
# The keys are typically strings or numbers, and the values can be any type of Python object.
# Dictionaries are also sometimes called "maps", "hash maps", or "associative arrays".

# Creating a dictionary
# You can create an empty dictionary like this:
empty_dict = {}

# Or you can initialize a dictionary with key-value pairs:
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}

# Accessing values in a dictionary
# You can access the value associated with a particular key using square bracket notation:
print(fruit_colors['apple']) # should print 'red'
print(fruit_colors['banana']) # should print 'yellow'

# If you try to access a key that doesn't exist, you'll get a KeyError:
# print(fruit_colors['orange']) # will raise a KeyError

# To avoid the KeyError, you can use the get() method instead:
print(fruit_colors.get('orange', 'unknown')) # should print 'unknown'

# Modifying values in a dictionary
# You can modify the value associated with a particular key like this:
fruit_colors['apple'] = 'green'
print(fruit_colors['apple']) # should now print 'green'

# Adding new key-value pairs
# You can add a new key-value pair to a dictionary like this:
fruit_colors['blueberry'] = 'blue'
print(fruit_colors['blueberry']) # should print 'blue'

# Removing key-value pairs
# You can remove a key-value pair from a dictionary using the del statement:
del fruit_colors['grape']
# print(fruit_colors['grape']) # will raise a KeyError

# Iterating over a dictionary
# You can use a for loop to iterate over the keys of a dictionary:
for fruit in fruit_colors:
    print(fruit)
# This will print 'apple', 'banana', and 'orange'.

# You can also use the items() method to get both the keys and values:
for fruit, color in fruit_colors.items():
    print(f'{fruit} is {color}')
# This will print 'apple is green', 'banana is yellow', and 'orange is orange'.

# Dictionary comprehensions
# Like list comprehensions, you can use a dictionary comprehension to create a new dictionary from an existing one:
fruits = ['apple', 'banana', 'orange']
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths) # should print {'apple': 5, 'banana': 6, 'orange': 6}