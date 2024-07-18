# User Input

# The input() function allows the user to input a value from the command line
# (also called the terminal). The value is stored as a string by default, so
# you might need to convert it to another data type.

name = input("What's your name? ")
age = input("How old are you? ")

# You can pass multiple arguments to a print() function and use + to
# concatenate them (stick them together).
print("Hello, " + name + ", you are " + age + " years old.")

# This method also works. The arguments will be separated by a space by
# default (you might not always want this).
print("My friend", name, "is", age, "years old.")

# Let's get a little more advanced. We're going to ask the user their birth
# year, and then tell them how old they are turning this year (2023).
# To do this, we'll need to use type conversion functions, specifically int()
# and str(), to change variables from one type to another.
birth_year = input("What year were you born in? ")
age = 2023 - int(birth_year)
print("You are turning " + str(age) + " years old this year!")

# In the code above, we first get the user's birth year. Since input() always
# returns a string, we need to use int() to convert the birth_year to an
# integer before we can use it in our calculation; you can't subtract a word
# from a number!
# We then calculate the user's age by subtracting their birth year from 2023,
# and store the result in the variable age.
# Finally, we use the str() function to convert the age to a string so we can
# concatenate it with the other strings in our print statement.
