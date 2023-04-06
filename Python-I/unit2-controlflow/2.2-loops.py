# Loops

# Loops are used to execute a block of code repeatedly, as long as a certain
# condition is met. There are "for" loops and "while" loops.

# For Loops
# Used to iterate over a sequence (such as a string, list, or tuple) and
# execute a block of code once per every item in the sequence.
fruits = ["strawberry", "lemon", "kiwi"]
for fruit in fruits:
    print(fruit)
    # The variable "fruit" is a substitute for each item in the list "fruits"

word = "sesquipedalian"
for char in word:
    print(char)
    # This will print every character in the string one line at a time

for i in range(1, 6):
    print(i)
    # range() is a built-in function that returns a sequence of numbers.
    # Here it takes at least two arguments: a start and a stop value.
    # The sequence will include the start value, but not the stop value.
    # This will print the numbers 1 through 5 (stops before 6).

for i in range(4):
    print(i)
    # If we don't include a start value, it defaults to zero.
    # This will print 0, 1, 2, and 3 (stops before 4).

for i in range(10, 20, 2):
    print(i)
    # We can include a third argument: the step value. In other words, how
    # many numbers we jump every time we increment. It's one by default.
    # This will print every even number between 10 and 20, excluding 20.

# While Loops
# Used to execute a block of code repeatedly, as long as a certain
# condition is true.
# Example:
i = 1
while i < 6:
    print(i)
    i += 1

# Loop Control Statements
# Used to change the execution from its normal sequence. Python has three
# loop control statements: 'break', 'continue', and 'pass'.

# break: Terminates the loop.
animals = ["sheep", "pig", "cow"]
for animal in animals:
    if animal == "pig":
        break
    print(animal)
    # This will print 'sheep' and then break out of the loop once it reaches 'pig'.

# Another example of a break statement in action:
numbers = [1, 3, 5, 4, 7, 9, 10, 11]
for num in numbers:
    if num % 2 == 0:
        print("The first even number is", num)
        break

# continue: Skips the current iteration of the loop and moves on to the next.
# Example:
trees = ["oak", "birch", "spruce"]
for tree in trees:
    if tree == "birch":
        continue
    print(tree)
    # This will print 'oak', skip 'birch', and print 'spruce'.

# pass: Used when you do not want any command or code to execute.
# Example:
metals = ["gold", "iron", "copper"]
for metal in metals:
    pass
    # Nothing will happen. 'pass' is sometimes used as a placeholder when
    # a statement is required for the rest of the code to execute.
    # Without the pass statement, Python would raise a SyntaxError.