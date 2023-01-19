# Manual string formatting
# The noob way
# Using the + symbol to concatenate strings and variables

def manual_str_format(name, age):
    print("My name is " + name + " and I am " + str(age) + " years old.")

manual_str_format("Hayden", 26)

# f-strings
# Easier to read and write

def f_str_format(name, age):
    print(f"My name is {name} and I am {age} years old.")

f_str_format("Hayden", 26)

# You can also put expressions inside of f-strings

print(f"{11 * 12}")