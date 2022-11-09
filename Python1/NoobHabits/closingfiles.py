# The less-effective way is to open the file, do stuff, then close it.
# But this introduces a problem.

def old_way(filename):
    f = open(filename, 'a')
    f.write("Hello!\n") # If an exception is thrown here, the file won't be closed.
    f.close()

# Instead, use "with" and "open":

def new_way(filename):
    with open(filename, 'a') as f:
        f.write("Hello!\n")

# The file automatically closes at the end of the "with" statement, regardless of an exception.

new_way("text.txt")