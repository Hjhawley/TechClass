# Brute forcing a max subsequence problem

A = [2, 3, -4, -2, 7, 1, -5, 3, 4, -10, 2, 4]

def maxSubsequence(A):
    bestT = A[0] # Max total, start with A[0] to ensure we get a valid return value
    bestS = 0 # Start
    bestE = 0 # End
    for s in range(len(A)):
        for e in range(s,len(A)): # Don't end before the start
            total = 0
            for i in range(s,e+1):
                total += A[i]
            if total > bestT:
                bestS = s
                bestE = e
                bestT = total
    return bestS, bestE

print(maxSubsequence(A))

# This is very inefficient. If we had a million items in the data set, this algorithm would take decades to finish.
# We can clean it up.

def maxSubsequence2(A):
    bestT = A[0] # Max total, start with A[0] to ensure we get a valid return value
    bestS = 0 # Start
    bestE = 0 # End
    for s in range(len(A)):
        for e in range(s,len(A)): # Don't end before the start
            total = 0
            '''
            for i in range(s,e+1): # Instead of recursively checking every single item, remember the previous sequence and simply compare the new one
                total += A[i]
                '''
            if total > bestT:
                bestS = s
                bestE = e
                bestT = total
    return bestS, bestE

print(maxSubsequence2(A))

# If the first algorithm takes 32 years, this one takes 16 minutes.