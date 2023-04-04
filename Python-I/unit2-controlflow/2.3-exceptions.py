# Exception Handling

# In programming, exceptions are errors that occur during program execution.
# Exception handling is the process of dealing with these errors in a clean
# and controlled manner.

# In Python, exceptions are objects that represent errors. When an error occurs,
# Python creates an exception object and "raises" it. If the exception is not
# handled (or "caught") by the program, it will cause the program to terminate
# (crash) and display an error message.

# To handle exceptions in Python, we use a try-except block. The code that might
# raise an exception goes in the "try" block, and the code that handles the
# exception goes in the "except" block.

# Example:
try:
    x = int("abcdefg")
except:
    print("Oops! That isn't a valid number.")
    
# In this example, we try to convert a string to an integer using the int()
# function, which will raise a ValueError exception. Because we have a try-except
# block, the program does not terminate, but instead prints a message to the console
# and continues.

# We can also catch multiple exceptions in the same try-except block, and we can
# use a "finally" block to execute code after the try-except block, regardless of
# whether an exception was raised or not.

# Example:
try:
    divisor = int(input("Give me a divisor. "))
    x = 100 / divisor
except ZeroDivisionError:   # Do this if a ZeroDivisionError is raised
    print("Oops! Cannot divide by zero.")
except:                     # Do this if any other error is raised
    print("Not a valid integer.")
else:                       # Do this if no errors are raised
    print(x)
finally:                    # Do this at the end, no matter what
    print("The code block is finished.")

# If the user inputs 0, the very next line will raise a ZeroDivisionError and the 
# program will print "Oops! Cannot divide by zero." If the user tries to input a
# string, the int() function will raise a ValueError which will result in
# "Not a valid integer." If the user inputs a valid non-zero number, the 'else'
# block will execute because no errors were raised. Regardless of what the user
# inputs, the 'finally' block will execute and print "The code block is finished."

# try-except blocks are an elegant solution for handling errors and edge cases,
# and it'd be wise to practice using them. Remember that tools like this are
# meant to make a programmer's life easier, not harder!