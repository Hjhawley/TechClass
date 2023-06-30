# Regular Expressions

# A regular expression, also known as regex, is a sequence of characters
# that defines a search pattern. It can be used to check if a string contains
# the specified search pattern.

# Python has a built-in module to work with regular expressions called 're'.
# Let's import it:
import re

# The 're' module offers a set of functions that allows us to search a string for
# a match:

# The 'findall' function returns a list containing all non-overlapping matches:
print(re.findall("a", "Hello, my name is Ana."))  # prints ['a', 'a']
# Note that it only counts lowercase 'a's and not the capital 'A'.

# The 'search' function searches the string for a match, and returns a Match object
# if there is a match. If there is more than one match, only the first occurrence 
# of the match will be returned:
match = re.search("a", "Hello, my name is Ana.")
print(match)  # prints <re.Match object; span=(11, 12), match='a'>

# The 'sub' function replaces all occurrences of the match with the text of your choice:
print(re.sub("a", "X", "Hello, my name is Ana."))  # prints 'Hello, my nXme is AnX.'

# We can use metacharacters, like [a-z] or [0-9], to find specific types of patterns:
# The following line prints all lowercase letters in the string
print(re.findall("[a-z]", "Hello, my name is Ana."))
# The following line prints all digits in the string
print(re.findall("[0-9]", "I have 2 apples and 3 oranges."))

# The 'split' function returns a list where the string has been split at each match of the pattern:
print(re.split("\s", "Split on spaces."))  # prints ['Split', 'on', 'spaces.']

# Regular expressions can get much more complex, but this is a basic introduction.