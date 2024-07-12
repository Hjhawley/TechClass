# Polymorphism

# Polymorphism is a feature of OOP that allows us to use methods interchangeably,
# even when different objects use those methods in different ways.
# This is useful in cases where different types of objects share a common interface but
# implement their behavior differently.

# For example:
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # This method is intended to be overridden in derived classes.
        raise NotImplementedError("Subclasses must implement this method")

# Derived classes
class Dog(Animal):
    def speak(self):
        return f"{self.name} says 'Woof'"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says 'Meow'"

class Bird(Animal):
    def speak(self):
        return f"{self.name} says 'Chirp'"

# Creating objects of derived classes
my_dog = Dog("Rascal")
my_cat = Cat("Cookie")
my_bird = Bird("Petey")

# Using polymorphism to call the same method on different objects
animals = [my_dog, my_cat, my_bird]

for animal in animals:
    print(animal.speak())

# Output:
#...

# Notice how polymorphism allows us to call the 'speak' method on each object,
# and each object responds appropriately according to its own implementation of the method.
