# Classes and Objects

# A class in Python is a blueprint for creating objects. It defines a set of
# attributes that characterize any object of the class.

# Defining a Simple Class
class Car:
    # The __init__ method is called the constructor. It's used for initializing
    # the attributes of the class.
    def __init__(self, brand, model, year):
        self.brand = brand  # Data member
        self.model = model  # Data member
        self.year = year    # Data member

    # A method for displaying car information
    def display_info(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}"

# Creating an Object
# To create an object, you call the class name followed by the data members you want to
# pass to the __init__ method as parameters.

my_car = Car("Toyota", "Corolla", 2020)  # Creating a Car object
print(my_car.display_info())  # Output: Car: Toyota Corolla, Year: 2020
