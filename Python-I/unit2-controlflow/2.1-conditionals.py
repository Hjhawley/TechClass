# Conditionals

# "if" statements help to control program flow based on certain conditions.
# The keyword "if" is followed by a logical expression which will return a
# boolean (True or False.) If the expression is True, the code block indented
# underneath the "if" statement will execute. If it's False, the code block
# underneath the "else" statement will execute.

age = int(input("What is your age? "))
if age < 18:
    print("You are not old enough to vote.")
else:
    print("You are old enough to vote.")
# The logical expression here is whether or not the user's age is at least 18.
# If they're under 18, the first print statement is what executes. If they're
# over 18, the second print statement is what executes.

# We can nest "if" statements within other "if" statements.
if age >= 16:
    if age >= 21:
        print("You can legally rent a car.")
    else:
        print("You can legally drive but can't rent a car.")
else:
    print("You are not old enough to drive.")

# We can include multiple conditional statements. The "elif" keyword stands
# for "else if" and is essentially the same as running another if statement.
x = int(input("Give me an integer. "))
if x > 0:
    print("That integer is positive.")
elif x == 0:
    print("That integer is zero.")
else:
    print("That integer is negative.")
# First we check if the variable is positive. If it's not, we check if it's
# exactly zero. Finally, if neither of those are true, we conclude that it
# must be negative.
# Wherever possible, "elif" statements are usually a more elegant and readable
# alternative to nested "if" statements, especially if you'd have multiple
# levels of nesting.

# By the way, there doesn't necessarily need to be an "else" statement.

myNum = int(input("Give me your favorite number. "))
print(f"Your favorite number is {myNum}.")
if myNum % 2 == 0:
    print("Your favorite number is even.")

# You can also use "if" statements to check for the presence of a value in a
# list or other sequence.
fruits = ['apple', 'banana', 'orange']
if 'apple' in fruits:
    print("You like apples!")
# This code will print "You like apples!" because 'apple' is in the 'fruits'
# list.

# A list is an ordered sequence of items enclosed in square brackets and
# separated by commas. The elements can be of different data types, such as
# integers, floats, strings, and even other lists. Lists allow for easy
# addition, removal, and modification of elements. We'll talk about them in
# more detail later on.