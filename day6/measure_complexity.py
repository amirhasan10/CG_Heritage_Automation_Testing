
# ── Hands-On 2.5: Empirically verify Big-O ────────────────────── 
import time, math 
  
def measure(fn, sizes): 
    for n in sizes: 
        data = list(range(n)) 
        start = time.perf_counter() 
        fn(data) 
        elapsed = (time.perf_counter() - start) * 1000 
        print(f'n={n:>8,}  →  {elapsed:8.3f} ms') 
  
# O(n) function 
def linear(arr): 
    total = 0 
    for x in arr: total += x 
    return total 
  
# O(n²) function 
def quadratic(arr): 
    count = 0 
    for i in arr: 
        for j in arr: 
            count += 1 
    return count 
  
print('--- O(n) ---') 
measure(linear, [1_000, 10_000, 100_000]) 
# n=    1,000  →  0.041 ms 
# n=   10,000  →  0.391 ms   (10× larger → ~10× slower ✓) 
# n=  100,000  →  3.820 ms 
  
print('--- O(n²) ---') 
measure(quadratic, [100, 1_000, 3_000]) 
# n=      100  →  0.54 ms 
# n=    1,000  →  54.2 ms    (10× larger → ~100× slower ✓) 
# n=    3,000  →  487  ms 
