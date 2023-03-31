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