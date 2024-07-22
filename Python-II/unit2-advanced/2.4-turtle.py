# Turtle Graphics

# Turtle graphics is a popular way for introducing programming to kids.
# It provides a visual way to learn programming concepts by drawing on the screen.

# The turtle module is included in the standard Python distribution and requires no installation.

# Importing the turtle module
import turtle

# Creating a turtle object
my_turtle = turtle.Turtle()

# Setting the speed of the turtle
my_turtle.speed(1)  # 1 is the slowest, 10 is the fastest, 0 is the fastest possible

# Moving the turtle forward
my_turtle.forward(100)  # Move forward by 100 units

# Turning the turtle
my_turtle.right(90)     # Turn right by 90 degrees

# Drawing a square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Changing the color of the turtle
my_turtle.color("blue")

# Drawing a triangle
for _ in range(3):
    my_turtle.forward(100)
    my_turtle.left(120)

# Writing text on the screen
my_turtle.penup()           # Lift the pen so it doesn't draw
my_turtle.goto(-50, 50)     # Move the turtle to a new location
my_turtle.pendown()         # Put the pen down to start drawing
my_turtle.write("Hello, world!", font=("Arial", 16, "normal"))

# Closing the turtle graphics window
turtle.done()
