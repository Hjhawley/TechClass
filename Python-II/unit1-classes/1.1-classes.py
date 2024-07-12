# Classes and Objects

# In OOP, a class is a blueprint for creating objects. It defines a set of
# attributes that characterize any object of the class.

# Defining a simple class
class Car:
    def __init__(self, brand, model, year, color):
        # The 'self' parameter is a reference to the current instance of the class.
        # It's used to access variables that belong to the class.
        self.brand = brand  # Data member: stores the brand of the car
        self.model = model  # Data member: stores the model of the car
        self.year = year    # Data member: stores the manufacturing year of the car
        self.color = color  # Data member: stores the color of the car

    def display_info(self):
        # Method: returns the car's information as a formatted string.
        return f"Car: {self.color} {self.year} {self.brand} {self.model}"

    def update_year(self, new_year):
        # Method: updates the year of the car.
        self.year = new_year

# Creating an object
# To create an object, you call the class name followed by the data members you want to
# pass to the __init__ method as parameters.

your_car = Car("Chevrolet", "Impala", 2015, "Silver")  # Creating a Car object
print(your_car.display_info())  # Output: Car: Silver 2015 Chevrolet Impala

# Objects can have their attributes updated using methods.
my_car = Car("Honda", "Accord", 2003, "White")
print(my_car.display_info())  # Output: Car: White 2003 Honda Accord
my_car.update_year(2021)      # Year updated to 2021
print(my_car.display_info())  # Output: Car: White 2021 Honda Accord

# Accessing attributes directly
# Although it's better practice to use methods, you can also access and modify attributes directly.
print(my_car.brand)  # Output: Honda
print(my_car.model)  # Output: Accord

# Directly modifying an attribute
my_car.color = "Black"
print(my_car.display_info())  # Output: Car: Black 2021 Honda Accord
