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

# Practice using turtle graphics by creating various shapes and patterns.
# Here are some additional exercises to try:
# 1. Draw a star
# 2. Draw a circle
# 3. Draw a hexagon
# 4. Create a pattern using different shapes and colors

# Example: Drawing a star
def draw_star(size, color):
    my_turtle.color(color)
    my_turtle.begin_fill()
    for _ in range(5):
        my_turtle.forward(size)
        my_turtle.right(144)
    my_turtle.end_fill()

# Drawing stars with different sizes and colors
my_turtle.penup()
my_turtle.goto(-200, -200)
my_turtle.pendown()
draw_star(100, "red")

my_turtle.penup()
my_turtle.goto(0, -200)
my_turtle.pendown()
draw_star(100, "green")

my_turtle.penup()
my_turtle.goto(200, -200)
my_turtle.pendown()
draw_star(100, "blue")

turtle.done()
