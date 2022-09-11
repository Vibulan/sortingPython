import random

def Merge(A, i, j, m):
    for k in A[i : m]:
        while m < j and k > A[m]:
            A[i] = A[m]
            i = i + 1
            m = m + 1
        A[i] = k
        i = i + 1

def MergeSortSlice(A, i, j):
    if j - i > 1:
        m = (i + j) // 2
        MergeSortSlice(A, i, m)
        MergeSortSlice(A, m, j)
        Merge(A, i, j, m)
        
def MergeSort(A):
    MergeSortSlice(A, 0, len(A))

A = []
for i in range(12):
    A.append(random.randint(-20, 20))

print(A)   
MergeSort(A)
print(A)

