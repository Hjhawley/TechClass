import math

def isPrime(x):
        s = int(math.sqrt(x))
        for i in range(2, s+1):
            if x % i == 0:
                return False
        return True

class HashTable:

    def __init__(self, desiredCount):
        actualCount = 2 * desiredCount + 1
        while not isPrime(actualCount):
            actualCount += 2                # Start at an odd number and skip the evens
        self.mTable = [None] * actualCount

    def exists(self, item):
        key = int(item)                     # We need to overload __int__ in our Student class
        index = key % len(self.mTable)      # This is where it's most likely to be
        while True:
            if self.mTable[index] is None:
                return False
            elif self.mTable[index] and self.mTable[index] == item:
                return True
            index += 1
            if index == len(self.mTable):   # Wrap around
                index = 0
    
    def insert(self, item):
        if self.exists(item):
            return False
        key = int(item)
        index = key % len(self.mTable)
        while self.mTable[index]:
            index += 1
            if index == len(self.mTable):
                index = 0
        self.mTable[index] = item
        return True
    
    def retrieve(self, item):
        if not self.exists(item):
            return None
        key = int(item)
        index = key % len(self.mTable)
        while not(self.mTable[index] and self.mTable[index] == item):
            index += 1
            if index == len(self.mTable):   # Wrap around
                index = 0
        return self.mTable[index]

    def delete(self, item):
        if not self.exists(item):
            return False
        key = int(item)
        index = key % len(self.mTable)
        while not (self.mTable[index] and self.mTable[index] == item):
            index += 1
            if index == len(self.mTable):   # Wrap around
                index = 0
        self.mTable[index] = False          # 'False' means there used to be something at this index, but there's not anymore.
        return True                         # This allows us to Delete items without tripping up the Exists function.

    def size(self):
        count = 0
        for i in self:
            if i:                           # In other words, if not "None" or "False"
                count += 1
        return count

    def traverse(self, callback, data):
        for i in self.mTable:
            if i:
                callback(i, data)