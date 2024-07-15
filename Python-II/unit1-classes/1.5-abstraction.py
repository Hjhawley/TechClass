# Abstraction

# Abstraction is a principle of OOP that involves hiding the complex implementation details of
# an object and showing only the essential features. It helps in reducing programming complexity
# and effort. In Python, abstraction can be achieved by defining methods in the base class
# that do not contain implementation, forcing subclasses to provide the implementation.

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
        super().__init__(color)
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
        super().__init__(color)
        self.radius = radius

    def area(self):
        # Implementing the abstract method
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        # Implementing the abstract method
        return 2 * 3.14 * self.radius

    def display_info(self):
        # Overriding the method to include additional information
        return f"A {self.color} circle with radius {self.radius}"

# Creating objects of the subclasses
rectangle = Rectangle(10, 20, "blue")
circle = Circle(15, "red")

# Using the methods to demonstrate abstraction
print(rectangle.display_info())                         # Output: A blue rectangle with width 10 and height 20
print(f"Rectangle Area: {rectangle.area()}")            # Output: Rectangle Area: 200
print(f"Rectangle Perimeter: {rectangle.perimeter()}")  # Output: Rectangle Perimeter: 60

print(circle.display_info())                            # Output: A red circle with radius 15
print(f"Circle Area: {circle.area()}")                  # Output: Circle Area: 706.5
print(f"Circle Perimeter: {circle.perimeter()}")        # Output: Circle Perimeter: 94.2
