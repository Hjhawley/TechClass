# There are many ways to manipulate strings in helpful ways.

# Concatenation - chaining two strings together
# We define two string variables str1 and str2, and use the + operator to concatenate
# them together, along with a space in between. The resulting string is stored in a new
# variable str3, which is then printed to the console.
str1 = "Hello"
str2 = "world"
str3 = str1 + " " + str2
print(str3)

# Slicing - extracting a portion of a string
# We define a string variable str4 and use square brackets [] to slice the string into
# substrings. We print out three different substrings of str4 using slicing.
# In Python, indexing starts at 0, so the first character of a string is at index 0,
# the second character is at index 1, and so on. When using slicing, you specify the
# starting index and the ending index of the substring you want to extract.
# The starting index is inclusive, meaning the character at that index will be included
# in the resulting substring. The ending index is exclusive, meaning the character at
# that index will not be included in the resulting substring.
str4 = "Python is awesome"
print(str4[0:6])  # Prints "Python" (characters 0-5)
print(str4[7:9])  # Prints "is" (characters 7-8)
print(str4[10:17])  # Prints "awesome" (characters 10-16)

# Formatting - insert values into a string
# There are several ways to do this:
# The % operator uses special formatting codes to insert values into the string.
# For example, %s is used to insert a string, %d for an integer, and %f for a float.
name = "John"
age = 25
print("My name is %s and I am %d years old." % (name, age))
# The str.format() method allows you to insert values into a string by positioning
# them inside curly braces {}. You can also use positional and keyword arguments to
# specify the values to be inserted.
name = "John"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
# f-strings are a relatively new and more concise way to format strings. They are
# formatted string literals that start with the letter f before the opening quote.
# You can insert variables and expressions directly into the string by wrapping them
# in curly braces {}.
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Additional tricks for formatting strings:

# The newline character, represented by \n, is the equivalent of hitting the enter key.
print("\nI \nlove \nPython")

print("\nThis makes sure the 'name' string is exactly 10 spaces wide.")
name = "Jill"
print("hello %10s." % (name))

print("\nThis left-pads an integer with zeros.")
i = 5
j = 15
print("%02d" % (i))
print("%02d" % (j))

print("\nThis supresses the return until afterwards.")
i = 5
j = 15
print("%02d" % (i), end = "")
print("%02d" % (j), end = "")
print()

print("\nThis prints a float that will take 6 spaces, with 2 right of the")
print("decimal left padded with zeros.")
x = 13.12345
print("%06.2f" % (x))

print("\nThis prints a string left justified, instead of its default, right justified.")
print("It's in a field 9 wide, and suppresses the return.")
name = "Jill"
x = name.ljust(9," ")

print (x,end="")