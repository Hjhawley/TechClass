# Build a basic calculator program. It needs to prompt the user for
# two numbers and an arithmetic operator (+, -, *, or /) and print
# the result. The program should continue until the user quits.

# Use "while True:" to loop the program until the user quits.

# Use "try:" and "except ValueError:" to handle invalid inputs.

# Prompt the user to input two numbers, num1 and num2, as well as
# an operator. Store these values as variables. num1 and num2 should
# be floats or ints, and operator should be a string.

# Check the operator using a series of if-elif-else statements. If
# the operator is one of the four standard arithmetic operators
# (+, -, *, /) perform the corresponding operation using num1 and num2
# and store the result in a variable called result. If the operator is
# division and num2 is equal to zero, print the message
# "Error: Division by zero" and use "continue".

# If the operator is the character "q", print the message
# "Exiting calculator" and break out of the infinite loop.

# If the operator is anything else, print the message
# "Invalid operator" and continue to the next iteration of the loop.

# If there are no errors, print the value of result using an f-string and the message "Result: {result}".
# If the user enters an invalid number, catch the ValueError and print the message "Invalid number" before continuing to the next iteration of the loop.

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /) or 'q' to quit: ")
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero")
                continue
            else:
                result = num1 / num2
        elif operator == "q":
            print("Exiting calculator")
            break
        else:
            print("Invalid operator.")
            continue
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input.")
        continue