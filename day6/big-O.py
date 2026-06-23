
def print_twice(arr): 
    for x in arr:  print(x)   # n operations 
    for x in arr:  print(x)   # n operations 
# Total: 2n  →  O(n)  (constants are dropped) 


def mixed(arr): 
    for i in arr:             # O(n) 
        for j in arr:         # O(n) 
            print(i, j)       # → O(n²) for nested loops 
    for x in arr:             # O(n) 
        print(x) 
# Total: n² + n  →  O(n²)  (n² dominates) 



def compare(arr_a, arr_b): 
    for a in arr_a:           # O(a) — size of arr_a 
        for b in arr_b:       # O(b) — size of arr_b 
            if a == b: 
                print('match') 
# This is O(a × b), NOT O(n²)! 
# If arr_a has 10 items and arr_b has 1 million items, 
# treating both as n gives a wildly wrong estimate. 
