arr = [1,2,1,0,1,1,0]
k = 4

left = 0
current_sum = 0
max_length = 0

for right in range(len(arr)):

    current_sum += arr[right]

    while current_sum > k:

        current_sum -= arr[left]

        left += 1

    max_length = max(max_length, right-left+1)

print("Longest Length =", max_length)