# Solving the Towers of Hanoi with recursion

def moveDisks(n, source, destination, other):
    if n == 1:
        print("Move one disk from", source, "to", destination)
    else:
        moveDisks(n-1, source, other, destination)
        moveDisks(1, source, destination, other)
        moveDisks(n-1, other, destination, source)

def main():
    n = 5
    moveDisks(n, 1, 2, 3)

main()