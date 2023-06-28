# Let's debug this piece of code:

def calculate_total(items):
    total = 0
    for item in items:
        total += item
    return total

items = [1, 2, 3, 4, 5]
total = calculate_total(items)
print(f"The total is {total}")

# Set a breakpoint at line 6, which is 'total += item'. Start the debugger.
# Look at the 'total' and 'item' variables on the left. Use "step over" to
# continue executing one line at a time, and watch how the variables change as you
# do. This is a great way to visualize your code and understand how it works.