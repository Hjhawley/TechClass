# Operator Overloading

# Operator overloading allows you to define how operators (see Python I - Lesson 1.4)
# behave with user-defined objects. For instance, when you use the + operator with integers 
# or strings, it performs addition and concatenation, respectively. With operator overloading,
# you can define how the + operator should behave with instances of your custom class.

# Python allows you to overload operators by defining special methods in your class. 
# These methods have double underscores (__) at the beginning and end of their names,
# also known as "dunder" methods.

# Here are some common operators and their corresponding dunder methods:
# - Addition: __add__(self, other)
# - Subtraction: __sub__(self, other)
# - Multiplication: __mul__(self, other)
# - Division: __truediv__(self, other)
# - String Representation: __str__(self)

# Example: Overloading the + Operator
# Let's start with an example where we create a Vector class that represents a vector in 2D space. 
# We'll overload the + operator to add two vectors together.

# Define a Vector class to represent a vector in 2D space
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the + operator
    def __add__(self, other):
        # Add corresponding components of the two vectors
        return Vector(self.x + other.x, self.y + other.y)

    # Overload the str operator to print the vector nicely
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Create two vectors
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Add the two vectors using the overloaded + operator
v3 = v1 + v2

# Print the result
print(v3)  # Output: Vector(6, 8)

# Exercise: Overloading More Operators
# Now it's your turn to practice operator overloading. Follow the instructions below to complete the exercises.

# Exercise 1: Subtraction and Multiplication
# 1. Add support for the - operator to the Vector class to subtract one vector from another.
# 2. Add support for the * operator to the Vector class to multiply a vector by a scalar (a number).

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        # Subtract corresponding components of the two vectors
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        # Multiply each component of the vector by the scalar
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Create vectors
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Subtract vectors
v4 = v1 - v2
print(v4)  # Output: Vector(-2, -2)

# Multiply vector by scalar
v5 = v1 * 3
print(v5)  # Output: Vector(6, 9)

# Exercise 2: Implement a Custom Class with Overloaded Operators
# Create a ComplexNumber class that represents a complex number with real and imaginary parts. 
# Overload the +, -, and * operators to perform addition, subtraction, and multiplication of complex numbers.

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __str__(self):
        return f"ComplexNumber({self.real} + {self.imag}i)"

# Create complex numbers
c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, 4)

# Add, subtract, and multiply complex numbers
c3 = c1 + c2
c4 = c1 - c2
c5 = c1 * c2

# Print results
print(c3)  # Output: ComplexNumber(4 + 6i)
print(c4)  # Output: ComplexNumber(-2 + -2i)
print(c5)  # Output: ComplexNumber(-5 + 10i)

# Summary
# In this lesson, we learned about operator overloading and how to use it to make custom classes work intuitively with Python's built-in operators. 
# We saw examples of overloading the +, -, and * operators for vector addition, subtraction, and scalar multiplication. 
# We also implemented a ComplexNumber class to handle operations on complex numbers.

# Practice using operator overloading with your own classes to make them more flexible and intuitive to use!
