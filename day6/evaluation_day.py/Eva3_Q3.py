import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [8,4,1,9,2,7]

start = time.time()

bubble_sort(arr)

end = time.time()

print("Sorted:", arr)
print("Execution Time =", end-start, "seconds")