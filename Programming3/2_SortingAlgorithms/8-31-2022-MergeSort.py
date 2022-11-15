A = [-2, 4, 6, -3, 7, 6, 8, 0, 2]

def mergeSort(A):
    if len(A) <= 1:
        return
    mid = len(A)//2
    L = A[:mid]
    R = A[mid:]
    # Sort L and R recursively
    mergeSort(L)
    mergeSort(R)
    # Merge L and R over A
    i = 0 # Left index
    j = 0 # Right index
    k = 0 # Merged index
    while i < len(L) and j < len(R): # Merge
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
            k+=1
        else:
            A[k] = R[j]
            j+=1
            k+=1
    # Add the leftovers
    while i < len(L):
        A[k] = L[i]
        i+=1
        k+=1
    while j < len(R):
        A[k] = R[j]
        j+=1
        k+=1

mergeSort(A)
print(A)