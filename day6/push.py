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