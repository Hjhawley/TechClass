# Write a program that converts Roman numerals to integers.

# Define a function called romanToInt that takes one parameter, a string,
# representing the Roman numeral which will be converted. Name it whatever
# you want as long as it's clear and helpful. For our purposes I'll just
# call it 's'.

# Inside the function, define a dictionary called roman_num (or something
# similar) that maps Roman numeral characters to their corresponding integer
# values. Here are the mappings:
'''
'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
'''

# Initialize a variable called result and set it to 0. This will be used to
# store the integer value of the Roman numeral.

# Loop through each character in the input string variable from left to right
# using a for loop and the range() and len() functions. We will assume each
# character is a valid Roman numeral and set up exception handling later.

# For each character 'i', we will initiate an if-else statement.
# If i is less than (len(s) - 1), and roman_num[s[i]] is less than
# roman_num[s[i + 1]], that means that a smaller character is coming before a
# larger character, like in the example IV which equals 4. In cases like this,
# we need to SUBTRACT roman_num[s[i]] from our result variable.
# Otherwise, we need to ADD roman_num[s[i]] from our result variable.
# Return the result.

# Define the main function. Use 'while True:' to loop until the user quits.
# Use a 'try-except' block to catch errors. This will make sure the user's inputs
# are all valid Roman numeral characters. Prompt them for a Roman numeral, and
# also tell them they can enter 'Q' to quit. Use the .upper() method so that
# the user's input can be lower or uppercase. Break from the loop if their
# input is 'Q'. Otherwise, call romanToInt and pass the user's input as the
# argument, and print the result. In the 'except' block, tell the user that
# they did not provide a valid input, and call main() again.

# Finally, call the main function.
