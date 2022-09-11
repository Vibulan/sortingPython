import random

def SelectionSort(A):
    for i in range(0, len(A)):
        min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j
        A[min], A[i] = A[i], A[min]

A = []
for i in range(12):
    A.append(random.randint(-20, 20))

print(A)
SelectionSort(A)
print(A)