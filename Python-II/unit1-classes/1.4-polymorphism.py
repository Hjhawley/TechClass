# Polymorphism

# Polymorphism is a feature of OOP that allows methods to be used interchangeably
# across different objects, even when these methods are implemented differently.
# This is useful when different types of objects share a common interface but
# implement their behavior in different ways.

# This concept is also called "Duck typing".
# "If it walks like a duck and it quacks like a duck, it must be a duck."
# This means that if an object implements the necessary methods, it can be used
# interchangeably regardless of its actual type.

# Here's an example of polymorphism:

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # This method is intended to be overridden in derived classes.
        raise NotImplementedError("Subclasses must implement this method")

# Derived class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says 'Woof'"

# Derived class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says 'Meow'"

# Derived class
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
# Rascal says 'Woof'
# Cookie says 'Meow'
# Petey says 'Chirp'

# Notice how polymorphism allows us to call the 'speak' method on each object,
# and each object responds according to its own implementation of the method.
