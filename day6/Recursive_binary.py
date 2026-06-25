# ── RECURSIVE BINARY SEARCH ──────────────────────────────────────────
def binary_search_recursive(arr, target, left, right):
    # BASE CASE 1: Search space exhausted
    if left > right:
        return -1
 
    mid = (left + right) // 2
 
    # BASE CASE 2: Target found
    if arr[mid] == target:
        return mid
 
    # RECURSIVE CASE: Search appropriate half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
 
# ── REAL-LIFE USE CASE: Find a student rank in sorted leaderboard ─────
leaderboard = [1200, 1450, 1600, 1750, 1800, 1920, 2050, 2200]
score_to_find = 1800
 
pos = binary_search_recursive(leaderboard, score_to_find, 0, len(leaderboard)-1)
print(f'Score {score_to_find} is at leaderboard rank {pos + 1}')  # Output: rank 5
 
# ── CALL STACK VISUALIZATION for arr=[1,3,5,7,9], target=7 ──────────
# Call 1: left=0, right=4, mid=2 → arr[2]=5 < 7 → go right
# Call 2: left=3, right=4, mid=3 → arr[3]=7 == 7 → return 3
# Call 1 gets 3 back → returns 3
