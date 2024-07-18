# File I/O

# Python has a built-in 'open' function for opening files. It takes two arguments:
# the name of the file, and the mode in which to open the file.

# Reading from a File

# Let's open a file in read mode ('r') and print its contents.
# Here's how you can do it:

with open('example.txt', 'r') as f:
    content = f.read()
    print(content)

# 'with' is a keyword in Python that's used in context management. It automatically
# closes the file when you're done with it. 'f' is the file object that we use to
# interact with the file.

# 'f.read()' reads the entire contents of the file and returns it as a string.

# If 'example.txt' does not exist in the current working directory, Python will raise a
# FileNotFoundError. This means that 'example.txt' needs to be in the same directory
# as this Python file, and you'll have to navigate to this directory from your terminal
# if you're not already there. You can do this using the 'cd' (change directory) command.

# Alternatively, you can use an absolute path to specify the exact location of the file,
# which might look something like this if you're using Windows:
# with open('C:\\Users\\username\\GitHub\\TechClass\\Python-I\\unit3-advanced\\example.txt', 'r') as f:

# Note the double backslashes (\\) used in the path string. In Python strings, the backslash is an escape character,
# so to represent a single backslash, you need to use two backslashes.

# Writing to a File

# Now let's write some text to a new file. To do this, we open a file in write mode ('w'):

with open('output.txt', 'w') as f:
    f.write("Hello, world!")

# If 'output.txt' didn't already exist, Python creates it. If it did exist, Python
# overwrites its contents before opening it for writing.

# 'f.write()' writes a string to the file.

# Appending to a File

# If you want to add to an existing file without deleting its content, open it in
# append mode ('a'):

with open('output.txt', 'a') as f:
    f.write("\nThis is an additional line.")

# Now 'output.txt' should contain two lines of text.
# The '\n' character represents a newline. It's how you create line breaks when
# writing to a file.
