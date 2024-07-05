# Classes and Objects

# A class in Python is a blueprint for creating objects. It defines a set of
# attributes that characterize any object of the class.

# Defining a Simple Class
class Car:
    def __init__(self, brand, model, year, color):
        # The 'self' parameter is a reference to the current instance of the class.
        # It's used to access variables that belong to the class.
        self.brand = brand  # Data member
        self.model = model  # Data member
        self.year = year    # Data member
        self.color = color  # Data member

    def display_info(self):
        # Returns the car's information as a formatted string.
        return f"Car: {self.color} {self.year} {self.brand} {self.model}"

    def update_year(self, new_year):
        # Updates the year of the car.
        self.year = new_year

# Creating an Object
# To create an object, you call the class name followed by the data members you want to
# pass to the __init__ method as parameters.

your_car = Car("Chevrolet", "Impala", 2015, "Silver")  # Creating a Car object
print(your_car.display_info())  # Output should be 'Car: Silver 2015 Chevrolet Impala'

# Objects can have their attributes updated using methods.
my_car = Car("Honda", "Accord", 2003, "White")
print(my_car.display_info())  # Output should be 'Car: White 2003 Honda Accord'
my_car.update_year(2021)      # Year updated to 2021
print(my_car.display_info())  # Output should be 'Car: White 2021 Honda Accord'

# Accessing attributes directly
print(my_car.brand)  # Output should be 'Honda'
print(my_car.model)  # Output should be 'Accord'

# You can also modify attributes directly, but it's better practice to use methods.
my_car.color = "Black"
print(my_car.display_info())  # Output: Car: Black 2021 Honda Accord
