# Inheritance

# Inheritance is a fundamental concept in OOP. 
# It allows you to define a class that inherits all the methods and properties from another class.

# The "parent" class is the class being inherited from, also called the base class.
# The "child" class is the class that inherits from another class, also called the derived class.

# Defining a parent class
class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def display_info(self):
        return f"{self.name} is a {self.category}"

# Defining a child class
class Bird(Animal):
    def __init__(self, name, category, can_fly):
        # Call the constructor of the parent class
        # The super() function allows us to call a method from the parent class
        # Here, it calls the __init__ method of the Animal class
        super().__init__(name, category)
        self.can_fly = can_fly  # Additional attribute for the Bird class

    def display_info(self):
        # Override the parent method
        info = super().display_info()
        if self.can_fly:
            return f"{info} and can fly."
        else:
            return f"{info} and cannot fly."

    def fly(self):
        if self.can_fly:
            return f"{self.name} is flying!"
        else:
            return f"{self.name} cannot fly."

# Defining a different child class
class Fish(Animal):
    def __init__(self, name, category, habitat):
        # Call the constructor of the parent class
        super().__init__(name, category)
        self.habitat = habitat  # Additional attribute for the Fish class

    def display_info(self):
        # Override the parent method
        return f"{super().display_info()} and lives in {self.habitat}."

    def swim(self):
        return f"{self.name} is swimming in {self.habitat}."

# Creating Objects
eagle = Bird("Eagle", "bird", 5, True)
penguin = Bird("Penguin", "bird", 3, False)
salmon = Fish("Salmon", "fish", 2, "freshwater")
clownfish = Fish("Clownfish", "fish", 1, "saltwater")

# Using Methods
print(eagle.display_info())     # Output: Eagle is a bird and can fly.
print(eagle.fly())              # Output: Eagle is flying!

print(penguin.display_info())   # Output: Penguin is a bird and cannot fly.
print(penguin.fly())            # Output: Penguin cannot fly.

print(salmon.display_info())    # Output: Salmon is a fish and lives in freshwater.
print(salmon.swim())            # Output: Salmon is swimming in freshwater.

print(clownfish.display_info()) # Output: Clownfish is a fish and lives in saltwater.
print(clownfish.swim())         # Output: Clownfish is swimming in saltwater.
