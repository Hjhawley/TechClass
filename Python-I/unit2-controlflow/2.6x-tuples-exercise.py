# Write a program that handles 3D coordinates.
# Given a list of 3D coordinates (x, y, z), write a function that finds the
# coordinate with the largest z value and returns it as a tuple.

# Example:
'''
Input: [(1, 2, 1), (10, 10, 12), (5, 15, 6), (7, 18, 9)]
Output: (10, 10, 12)
'''

# Define a function for finding the largest z coordinate in a ist of tuples.
# Initialize the largest_z_coord to the first coordinate in the list, assuming
# it has the largest z value so far. Loop through each coordinate in the input
# list using a for loop. For each coordinate, extract the x, y, and z values.
# Compare the z value of the current coordinate with the z value of the
# largest_z coordinate, which is largest_z[2]. If the z value of the current
# coordinate is greater than the z value of the largest_z coordinate, update the
# largest_z variable with the current coordinate. After the loop finishes,
# return largest_z.

# Outside the function, create a list of coordinates, and call the function you
# defined with this list as input. Print the output.
