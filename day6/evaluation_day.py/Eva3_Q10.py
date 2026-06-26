import time

def bubble_sort(arr):

    comparisons = 0

    n = len(arr)

    for i in range(n):

        for j in range(n-i-1):

            comparisons += 1

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

    return comparisons

arr = list(map(int,input("Enter numbers: ").split()))

copy = arr.copy()

start = time.time()

comparisons = bubble_sort(copy)

end = time.time()

print("\nOriginal Array:", arr)

print("Sorted Array:", copy)

print("Comparisons:", comparisons)

print("Execution Time:", end-start)

print("\nBig-O Analysis")

print("Best Case : O(n)")

print("Average Case : O(n²)")

print("Worst Case : O(n²)")