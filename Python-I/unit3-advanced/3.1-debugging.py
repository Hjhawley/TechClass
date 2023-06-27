# Debugging

# Debugging is an essential skill for any developer. It helps you to understand
# why your code is not working as expected. In Python, there are several debugging 
# techniques like using print statements, using Python's built-in debugger 'pdb', 
# or using debugging tools provided by your IDE.

# Debugging using Print Statements
# One of the simplest ways to debug is to print out the variables at certain stages of 
# the program to check their values.

def add_numbers(x, y):
    print(f"Adding {x} and {y}")
    result = x + y
    print(f"The result is {result}")
    return result

add_numbers(5, 3)  # Prints "Adding 5 and 3" and "The result is 8"

# Debugging with IDEs
# VS Code has a built-in debugging tool, like most IDEs.
# Click on the 'Run' menu, then 'Start Debugging', or press F5.
# In the left panel you'll see variables, call stack, and breakpoints.

# Breakpoints can be added by clicking next to the line number in the code editor.
# You should see a red dot. This is a breakpoint. You can add as many as you want.
# The debugger will pause execution at these points, letting you inspect variables 
# and control the execution flow.

# Let's debug a piece of code:

def calculate_total(items):
    total = 0
    for item in items:
        total += item
    return total

items = [1, 2, 3, 4, 5]
total = calculate_total(items)
print(f"The total is {total}")

# Set a breakpoint at line 35, which is 'total += item'. Start the debugger.
# Look at the 'total' and 'item' variables on the left. Use "step over" to
# continue executing one line at a time, and watch how the variables change as you
# do. This is a great way to visualize your code and understand how it works.