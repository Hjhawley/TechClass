# This way of doing it may seem more intuitive for beginners,
# but it's redundant and cluttered.

def range_len():
    a = [1, 2, 3]
    for i in range(len(a)):
        v = a[i]
        print(v)

# Instead of looping over each index, just grab the elements
# directly from the container.

def range_len():
    a = [1, 2, 3]
    for v in a:
        print(v)