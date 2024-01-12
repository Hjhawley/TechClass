# Classes and Objects

# A class in Python is a blueprint for creating objects. It defines a set of
# attributes that characterize any object of the class.

# Defining a Simple Class
class Car:
    # The __init__ method is called the constructor. It's used for initializing
    # the attributes of the class.
    def __init__(self, brand, model, year, color):
        self.brand = brand  # Data member
        self.model = model  # Data member
        self.year = year    # Data member
        self.color = color  # Data member

    # A method for displaying car information
    def display_info(self):
        return f"Car: {self.color} {self.year} {self.brand} {self.model}"

    # A method to update the year
    def update_year(self, new_year):
        self.year = new_year

# Creating an Object
# To create an object, you call the class name followed by the data members you want to
# pass to the __init__ method as parameters.

your_car = Car("Toyota", "Corolla", 2019, "Silver")  # Creating a Car object
print(your_car.display_info())  # Silver 2019 Toyota Corolla

# Objects can have their attributes updated using methods.

my_car = Car("Honda", "Accord", 2003, "White")
print(my_car.display_info())    # Car: White 2003 Honda Accord
my_car.update_year(2021)        # Year updated to 2021
print(my_car.display_info())    # Car: White 2021 Honda Accord