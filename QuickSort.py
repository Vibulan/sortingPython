# Pivot is the last element

import random

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
        p = Partition(A, i, j)
        QuickSortSlice(A, i, p)
        QuickSortSlice(A, p + 1, j)
        
def QuickSort(A):
    QuickSortSlice(A, 0, len(A))
    
A = []
for i in range(12):
    A.append(random.randint(-20, 20))

print(A)   
QuickSort(A)
print(A)