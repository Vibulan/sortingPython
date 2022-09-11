# Quicksort with randomized partition

import random

def RandomizedPartiton(A, i, j):
    p = random.randint(i, j - 1)
    A[p], A[j - 1] = A[j - 1], A[p]
    return Partition(A, i, j)

def Partition(A, i, j):
    pivot = A[j - 1]
    p = i
    for x in range(i, j - 1):
        if A[x] <= pivot:
            A[x], A[p] = A[p], A[x]
            p += 1
    A[p], A[j - 1] = A[j - 1], A[p]
    return p

def QuickSortSlice(A, i, j):
    if (j - i) > 1:
        p = RandomizedPartiton(A, i, j)
        QuickSortSlice(A, i, p)
        QuickSortSlice(A, p + 1, j)
        
def QuickSort(A): # Wrapper Function
    QuickSortSlice(A, 0, len(A))
    
A = []
for i in range(12):
    A.append(random.randint(-20, 20))

print(A)   
QuickSort(A)
print(A)
