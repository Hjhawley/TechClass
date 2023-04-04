# Tuples

# Tuples are another container data type.
# They are ordered, immutable collections of elements.
# They are similar to lists, but once created, their values cannot be changed.
# Tuples are defined using parentheses instead of square brackets.

# Example:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Accessing tuple elements is similar to accessing list elements.
# Example:
print(my_tuple[0]) # Should print 1
print(my_tuple[2:4]) # Should print (3, 4)

# You can also use tuples to return multiple values from a function.
# Example:
def calculate_statistics(numbers):
    count = len(numbers)
    total = sum(numbers)
    mean = total / count
    variance = sum((x - mean) ** 2 for x in numbers) / count
    standard_deviation = math.sqrt(variance)
    return count, total, mean, variance, standard_deviation

result = calculate_statistics([1, 2, 3, 4, 5])
print(result) # Should print (5, 15, 3.0, 2.0, 1.4142135623730951)

# You can unpack tuples by assigning their values to variables.
# Example:
count, total, mean, variance, standard_deviation = result
print(mean) # Should print 3.0

# Tuples can also be used as keys in dictionaries.
# Example:
my_dict = {
    (1, 2): 'hello',
    (3, 4): 'world'
}
print(my_dict[(1, 2)]) # Should print 'hello'