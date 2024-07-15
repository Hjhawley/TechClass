# Abstraction

# Abstraction is a principle of OOP that involves hiding the complex implementation details of
# an object and showing only the essential features. It helps in reducing programming complexity
# and effort. In Python, abstraction can be achieved by defining methods in the base class
# that do not contain implementation, forcing subclasses to provide the implementation.

import math  # We'll need this later

# Base class with common data members and abstract methods
class Shape:
    def __init__(self, color):
        self.color = color  # Common attribute for all shapes

    def area(self):
        # Abstract method, needs to be implemented by subclasses
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        # Abstract method, needs to be implemented by subclasses
        raise NotImplementedError("Subclasses must implement this method")

    def display_info(self):
        # Common method that can be overridden by subclasses
        return f"A {self.color} shape"

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)  # Call the constructor of the base class
        self.width = width
        self.height = height

    def area(self):
        # Implementing the abstract method
        return self.width * self.height

    def perimeter(self):
        # Implementing the abstract method
        return 2 * (self.width + self.height)

    def display_info(self):
        # Overriding the method to include additional information
        return f"A {self.color} rectangle with width {self.width} and height {self.height}"

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)  # Call the constructor of the base class
        self.radius = radius

    def area(self):
        # Implementing the abstract method
        return int(math.pi * self.radius ** 2)

    def perimeter(self):
        # Implementing the abstract method
        return int(2 * math.pi * self.radius)

    def display_info(self):
        # Overriding the method to include additional information
        return f"A {self.color} circle with radius {self.radius}"

# Creating objects of the subclasses
my_rectangle = Rectangle(10, 20, "blue")
my_circle = Circle(15, "red")

# Using the methods to demonstrate abstraction
print(my_rectangle.display_info())                         # Output: A blue rectangle with width 10 and height 20
print(f"Rectangle Area: {my_rectangle.area()}")            # Output: Rectangle Area: 200
print(f"Rectangle Perimeter: {my_rectangle.perimeter()}")  # Output: Rectangle Perimeter: 60

print(my_circle.display_info())                            # Output: A red circle with radius 15
print(f"Circle Area: {my_circle.area()}")                  # Output: Circle Area: 706
print(f"Circle Perimeter: {my_circle.perimeter()}")        # Output: Circle Perimeter: 94
