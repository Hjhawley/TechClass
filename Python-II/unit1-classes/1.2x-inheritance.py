# Create classes that model real-world objects using inheritance. Initialize objects from these classes 
# and implement methods to interact with the object attributes.

# Task 1: Define a Base Class
# Define a base class called `Appliance` with the following attributes:
# - name (a string)
# - brand (a string)
# 
# Add a method `display_info` to the `Appliance` class that returns a string with the appliance's name and brand.

# Task 2: Define Child Classes
# Define two child classes that inherit from `Appliance`:
# - `WashingMachine`
#   - Additional attribute: `load_capacity` (an integer)
#   - Method: `wash_clothes`, which prints a message about washing clothes with the load capacity.
# - `Refrigerator`
#   - Additional attribute: `temperature` (an integer)
#   - Method: `cool_food`, which prints a message about cooling food with the temperature.
# 
# Make sure that the `display_info` method in each child class includes information about the extra attribute.

# Task 3: Initialize Objects
# Create objects of both `WashingMachine` and `Refrigerator` classes with appropriate values.
# Example: 
# washer = WashingMachine(name="Super Wash 3000", brand="WashCorp", load_capacity=7)
# fridge = Refrigerator(name="CoolKeeper", brand="CoolBrand", temperature=4)

# Task 4: Use the Methods
# Use the `display_info`, `wash_clothes`, and `cool_food` methods on your objects and print the results.
# Example:
# print(washer.display_info())
# washer.wash_clothes()
# print(fridge.display_info())
# fridge.cool_food()

# Define your base class Appliance here


# Define your child class WashingMachine here


# Define your child class Refrigerator here


# Create objects of WashingMachine and Refrigerator here


# Use the methods and print the results here
