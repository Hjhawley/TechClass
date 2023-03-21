var = "blue"
print(var)

myAge = input("How old are you? ")
print("You are " + str(myAge) + " years old.")

birthYear = input("What year were you born? ")
birthYear = int(birthYear)
myAge = 2023 - birthYear
print("You will turn " + str(myAge) + " years old this year.")

# This is a comment. Python doesn't do anything with it. It's meant for humans to read.

"This is a string. It's an array of characters, like numbers and letters."

print("This is a print statement. We are telling Python to print the string inside of the parentheses.")

# print() is a built-in Python function.
# Functions can do all sorts of things.
# We can create our own functions as well.

def dumbFunction(word, number): # This is how we define a function. 
    print(word * number)

dumbFunction("Cheese", 3) # This is a function call. We are using the function that we just created.

# Hit the F5 key to run the program, then look at the terminal down below.