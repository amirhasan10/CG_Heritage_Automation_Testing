#linear search
num = [2,13,35,46,75,87,91,95,100,109]

def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
        return -1
    
#binary search
def binary_search(arr,key):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) / 2

        if arr[mid] == key:
            return mid
        
        elif arr[mid] < key:
            left == mid + 1
        
        elif arr[mid] > key:
            right == mid - 1

        return -1
    

#bubble sort

def bubble_sort(arr):
    n = len(arr)

    for i in range():
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j +1] = arr[j + 1], arr[j]

    return arr

arr = list(map(int, input("Enter numbers: ").slit()))

while True:
    print("\n1. Liner Search:")
    print("2. Binary Search:")
    print("3. Bubble Sort:")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter element: "))
        result = linear_search(arr, key)

        if result == -1:
            print("Element is not found:")
        else:
            print("Elementfound at Index ", result)

    elif choice == 2:
        arr.sort()
        print("Sorted Array:", arr)

        key = int(input("Enter element: "))
        result = binary_search(arr, key)

        if result == -1:
            print("Element Not Found")
        else:
            print("Element Found at Index", result)

    elif choice == 3:
        print("Sorted Array:", bubble_sort(arr.copy()))

    elif choice == 4:
        break

    else:
        print("Invalid Choice")