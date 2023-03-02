A = [-2, 4, 6, -3, 7, 6, 8]

def findValue(A,v):
    for i in range(len(A)):
        if A[i] == v:
            return i
    return -1

print(findValue(A,6))