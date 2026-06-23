
# ── Hands-On 1.4: Why DSA Matters ────────────────────────────── 
import time 
  
# Dataset: 1 million records (simulating a database of user IDs) 
data_list = list(range(1_000_000))   # List  → O(n) search 
data_set  = set(range(1_000_000))    # Set   → O(1) search (hash table) 
 
  
target = 999_999   # worst-case: target is at the very end 
  
# ── Approach 1: Linear scan through a List ── 
start = time.perf_counter() 
found = target in data_list          # Python checks element by element 
list_time = time.perf_counter() - start 
  
# ── Approach 2: Hash lookup in a Set ── 
start = time.perf_counter() 
found = target in data_set           # Python computes hash → direct jump 
set_time = time.perf_counter() - start 
  
print(f'List search : {list_time*1000:.4f} ms') 
print(f'Set  search : {set_time *1000:.6f} ms') 
print(f'Set is {list_time/set_time:.0f}x faster') 
  
# Typical output: 
# List search : 8.4231 ms 
# Set  search : 0.0012 ms 
# Set is ~7000x faster 
