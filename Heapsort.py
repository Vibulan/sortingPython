import random

def maxHeapify(arr, size, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    
    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, size, largest)
    

def Heapsort(arr):
    size = len(arr)
    for i in range(size // 2 - 1, -1,  -1):
        maxHeapify(arr, size, i)
    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        maxHeapify(arr, i, 0)

arr = []
for i in range(12):
    arr.append(random.randint(-20, 20))      

print(arr)
Heapsort(arr)
print(arr)