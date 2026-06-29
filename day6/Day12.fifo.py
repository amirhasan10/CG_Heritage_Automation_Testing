# ============================================================ 
#  COMPLETE STACK IMPLEMENTATION USING PYTHON LIST 
# ============================================================ 
  
class Stack: 
    """A LIFO Stack implemented using Python list.""" 
  
    def __init__(self): 
        self._data = []        # Internal list — end = TOP 
  
    def push(self, item): 
        """Add item to the TOP of the stack.  Time: O(1)""" 
        self._data.append(item)     # append() → adds to END (top) 
  
    def pop(self): 
        """Remove & return TOP item.  Time: O(1)""" 
        if self.is_empty(): 
            raise IndexError("pop from an empty stack") 
        return self._data.pop()     # pop() → removes from END (top) 
  
    def peek(self): 
        """Return TOP item WITHOUT removing.  Time: O(1)""" 
        if self.is_empty(): 
            raise IndexError("peek from an empty stack") 
        return self._data[-1]       # Index -1 = last element = top 
  
    def is_empty(self): 
        """Return True if no elements in stack.  Time: O(1)""" 
        return len(self._data) == 0 
  
    def size(self): 
        """Return count of elements.  Time: O(1)""" 
        return len(self._data) 
  
    def __repr__(self): 
        if self.is_empty(): 
            return "Stack: [EMPTY]" 
        return f"Stack [bottom→top]: {self._data}" 