# Create a fresh stack 
book_stack = [] 
  
# Push books one at a time (simulating placing on a desk) 
book_stack.push("Python Basics")       # First book — goes to bottom 
book_stack.push("Data Structures") 
book_stack.push("Algorithms") 
book_stack.push("System Design") 
book_stack.push("Clean Code")          # Last book — sits on TOP 
  
print(book_stack)                       # Show state 
print(f'Total books stacked: {book_stack.size()}') 
print(f'Top book right now: {book_stack.peek()}') 
# PEEK — see what's on top without disturbing the stack 
print(f'Peeking: {book_stack.peek()}')      # Clean Code (top) 
  
# POP — remove books in LIFO order 
print(f'\n--- Removing books one by one (LIFO) ---') 
removed = book_stack.pop() 
print(f'Removed: {removed:<20} | Stack size: {book_stack.size()}') 
  
removed = book_stack.pop() 
print(f'Removed: {removed:<20} | Stack size: {book_stack.size()}') 
  
removed = book_stack.pop() 
print(f'Removed: {removed:<20} | Stack size: {book_stack.size()}') 
  
print(f'\nRemaining: {book_stack}') 
print(f'Is empty? {book_stack.is_empty()}') 
  
# Remove last 2 books 
book_stack.pop()   # Data Structures 
book_stack.pop()   # Python Basics 
  
print(f'\nNow is empty? {book_stack.is_empty()}') 
  
# Try popping from empty stack 
try: 
    book_stack.pop() 
except IndexError as e: 
    print(f'Error caught: {e}') 