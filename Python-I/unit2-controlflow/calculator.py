# Build a basic calculator program. It needs to prompt the user for
# two numbers and an arithmetic operator (+, -, *, or /) and print
# the result. The program should continue until the user quits by
# entering "q".

# Hint: use 'while True:' to loop the program until the user quits.
# Use 'try' and 'except' to handle zero division and invalid numbers.

while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        operation = input("Enter operation (+,-,*,/): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Division by zero!")
            result = num1 / num2
        else:
            print("Invalid operation!")
            continue

        print(f"{num1} {operation} {num2} = {result}")
        
        choice = input("Do you want to continue (y/n): ")
        if choice.lower() == 'n':
            break
    except ValueError:
        print("Please enter valid numbers!")
    except ZeroDivisionError as error:
        print(error)