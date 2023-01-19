class Stack:

    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)

    def isEmpty(self):
        return len(self.data) == 0

    def top(self):
        if not self.isEmpty():
            return self.data[len(self.data)-1]

    def pop(self):
        return self.data.pop()