
# ── O(1) Examples ─────────────────────────────────────────────── 
  
# 1. Array index access 
fruits = ['apple', 'banana', 'cherry', 'date'] 
print(fruits[2])   # 'cherry' — instant, no matter how long the list 
  
# 2. Hash map lookup (Python dict) 
user_ages = {'Alice': 30, 'Bob': 25, 'Charlie': 35} 
print(user_ages['Bob'])  # O(1) — hash function jumps directly to bucket 
  
# 3. Arithmetic formula (no loops) 
def sum_of_n(n): 
    return n * (n + 1) // 2   # Gauss formula — always 1 multiplication + 1 division 
  
print(sum_of_n(1_000_000))  # Instant vs looping 1M times 
  
# 4. Stack operations 
stack = [] 
stack.append(10)    # O(1) push 
stack.append(20) 
top = stack.pop()   # O(1) pop → returns 20 
  
# Real-life: browser Back button is a stack! 
# Each page you visit is pushed. Back = pop. 
