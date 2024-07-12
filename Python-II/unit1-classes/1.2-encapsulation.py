# Encapsulation

# Encapsulation is one of the fundamental concepts of OOP.
# It means keeping data and the methods that work on that data bundled together in one class.
# This protects the data from being modified by accident and keeps the object reliable.

# Some programming languages like Java and C++ have strict access control keywords like 
# 'public', 'private', and 'protected' to enforce encapsulation.
# In Python, we use underscores (_) to indicate that an attribute is meant to be private.
# This is just a convention, not a strict rule enforced by Python.
# However, using this convention can help remind you and others how to treat the data.

# Defining a class with encapsulation
class Car:
    def __init__(self, brand, model, year, color):
        # Private attributes are defined with a leading underscore.
        self._brand = brand  # Private attribute
        self._model = model  # Private attribute
        self._year = year    # Private attribute
        self._color = color  # Private attribute

    # Public method to access the private attribute _brand
    def get_brand(self):
        return self._brand

    # Public method to modify the private attribute _brand
    def set_brand(self, brand):
        self._brand = brand

    # Public method to access the private attribute _model
    def get_model(self):
        return self._model

    # Public method to modify the private attribute _model
    def set_model(self, model):
        self._model = model

    # Public method to access the private attribute _year
    def get_year(self):
        return self._year

    # Public method to modify the private attribute _year
    def set_year(self, year):
        self._year = year

    # Public method to access the private attribute _color
    def get_color(self):
        return self._color

    # Public method to modify the private attribute _color
    def set_color(self, color):
        self._color = color

    def display_info(self):
        # Method: returns the car's information as a formatted string.
        return f"Car: {self._color} {self._year} {self._brand} {self._model}"

# Creating an object
my_car = Car("Toyota", "Camry", 2018, "Blue")

# Accessing and modifying private attributes using public methods
print(my_car.display_info())  # Output: Car: Blue 2018 Toyota Camry

# Updating attributes using setter methods
my_car.set_year(2022)
my_car.set_color("Red")
print(my_car.display_info())  # Output: Car: Red 2022 Toyota Camry

# Accessing attributes using getter methods
print(my_car.get_brand())  # Output: Toyota
print(my_car.get_model())  # Output: Camry

# Direct access to private attributes is discouraged.
# Example of what NOT to do:
#   my_car._year = 2025

# Instead, write a method within the class to update the year:
#   my_car.set_year(2025)
