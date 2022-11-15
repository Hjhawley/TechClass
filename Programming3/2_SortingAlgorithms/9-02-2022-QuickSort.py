'''Sidenote
Traveling saleseperson needs to figure out the quickest route
If there are 10 cities including the hometown, there are 9 options for the first destination, 8 for the next, etc
9 factorial, or (N-1)! which is even worse than the Towers of Hanoi problem (2^N)
"Kind of" proven to be an insolvable algorithm beyond brute-forcing, which is difficult and becomes impossible very quickly '''

# Quick sort
# N * log2(N) same as the merge sort at first glance, but fewer swaps.
# But worst case scenario is a list that's already mostly sorted, because it becomes N^2
# If you KNOW the list is mostly sorted, you want to use the shaker sort.

A = [-2, 4, 6, -3, 7, 6, 8, -2, 4, 6, -3, 7, 6, 8]

# First number (low) is called the pivot item

def quickSort(A, low, high):
    if high - low <= 0:
        return # Kill the loop if the list is only 1 item long
    lmgt = low + 1 # Leftmost of the greater-thans
    for i in range(low + 1, high + 1): # Everything except for the first list item (the pivot point)
        if A[i] < A[low]:
            A[i], A[lmgt] = A [lmgt], A[i] # Swap the item into the less-than side
            lmgt += 1
    pivot = lmgt - 1
    A[low], A[pivot] = A[pivot], A[low]
    quickSort(A, low, pivot-1) # Recurse on both sides
    quickSort(A, pivot+1, high)

# Modified

def modifiedQuickSort(A, low, high):
    if high - low <= 0:
        return
    mid = (low + high)//2           # Modified
    A[low],A[mid] = A[mid],A[low]   # Modified
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        if A[i]<A[low]:
            A[i],A[lmgt] = A [lmgt],A[i]
            lmgt += 1
    pivot = lmgt - 1
    A[low],A[pivot] = A[pivot],A[low]
    modifiedQuickSort(A, low, pivot-1)
    modifiedQuickSort(A, pivot+1, high)

modifiedQuickSort(A, 0, 13)
print(A)