import random

def InsertionSort(A):
    for j in range(2, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
     
A = []
for i in range(12):
    A.append(random.randint(-20, 20))
print(A)
InsertionSort(A)
print(A)
print(A)