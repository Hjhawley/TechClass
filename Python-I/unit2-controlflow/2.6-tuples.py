# Tuples

# Tuples are another container data type. They are ordered like lists, but unlike
# lists, they are immutable. They are similar to lists, but once created, their
# values cannot be changed. Tuples are defined using parentheses () instead of 
# square brackets [].

# Example:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Accessing tuple elements is similar to accessing list elements.
# Example:
print(my_tuple[0]) # Prints 1
print(my_tuple[2:4]) # Prints (3, 4)

# You can also use tuples to return multiple values from a function.
# Example:
def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

result = calculate_rectangle(5, 3)
print("Area:", result[0])
print("Perimeter:", result[1])

# We could also do it this way:
area, perimeter = calculate_rectangle(6, 4)
print("Area:", area)
print("Perimeter:", perimeter)
