# Build a basic calculator program. It needs to prompt the user for
# two numbers and an arithmetic operator (+, -, *, or /) and print
# the result. The program should continue until the user quits.

# Use "while True:" to loop the program until the user quits.

# Use "try:" and "except ValueError:" to handle invalid inputs and
# "except ZeroDivisionError" to handle division by zero. Be sure to
# tell the user what error was raised.

# Prompt the user to input two numbers, num1 and num2, as well as
# an operator. Store these values as variables. num1 and num2 should
# be cast to ints or floats using int() or float().

# Check the operator using a series of if-elif-else statements. If
# the operator is one of the four standard arithmetic operators
# (+, -, *, /) perform the corresponding operation using num1 and num2
# and store the result in a variable called result.

# If the operator is the character "q", print the message
# "Exiting calculator" and break out of the infinite loop.

# If the operator is anything else, print the message
# "Invalid operator" and continue to the next iteration of the loop.

# If there are no errors, print the value of result using an f-string 
# and the message "Result: {result}".