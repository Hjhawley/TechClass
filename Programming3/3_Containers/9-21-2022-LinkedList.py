class Student:
    def __init__(self, name, age) -> None:
        self.mName = name
        self.mAge = age
        # etc

class Node:
    def __init__(self, item, next) -> None:
        self.mItem = item
        self.mNext = next

def main():
    first = None
    s1 = Student('Ryan', '20')
    n = Node(s1, None)
    first = n
    s2 = Student('Hayden', '26')
    first = Node(s2, first) # assign the new item's next to be the previous item's address BEFORE changing "first"

'''
# Traverse
current = first
age = 0
while current: # or 'while current is not None'
    age += int(current.mAge)
    current = current.mNext
'''