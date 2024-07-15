# {provide an overview of this exercise}

# Task 1: Define a Base Class
# Define a base class called `Instrument` with the following attributes:
# - name (a string)
# - material (a string)
# Add abstract methods:
# - play_sound: should raise NotImplementedError
# - tune: should raise NotImplementedError
# Add a method `display_info` to the `Instrument` class that returns the name and material as a string.

# Task 2: Define Child Classes
# Define two child classes that inherit from `Instrument`:
# - `Guitar`
#   - Additional attribute: `number_of_strings` (an integer)
#   - Implement the `play_sound` and `tune` methods to print messages about playing and tuning the guitar.
#   - Override the `display_info` method to include the number of strings.
# - `Flute`
#   - Additional attribute: `type` (a string, e.g., "Transverse", "Recorder")
#   - Implement the `play_sound` and `tune` methods to print messages about playing and tuning the flute.
#   - Override the `display_info` method to include the type of flute.

# Task 3: Initialize Objects
# Create objects of both `Guitar` and `Flute` classes with appropriate values.
# Example:
# my_guitar = Guitar(name="Acoustic Guitar", material="Wood", number_of_strings=6)
# my_flute = Flute(name="Silver Flute", material="Silver", type="Transverse")

# Task 4: Use the Methods
# Use the `display_info`, `play_sound`, and `tune` methods on your objects 
# and print the results.
# Example:
# print(my_guitar.display_info())
# my_guitar.play_sound()
# my_guitar.tune()
# print(my_flute.display_info())
# my_flute.play_sound()
# my_flute.tune()

# Define your parent class Instrument here


# Define your child class Guitar here


# Define your child class Flute here


# Create objects of Guitar and Flute here


# Use the methods and print the results here
