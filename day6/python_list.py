# Python list can hold mixed types
try:
    import numpy as np  # type: ignore[import]
except ImportError:
    np = None

my_list = [42, 'hello', 3.14, True, [1,2,3]]
 
# Internal memory: list stores pointers (8 bytes each on 64-bit system)
# [ptr→42] [ptr→'hello'] [ptr→3.14] [ptr→True] [ptr→[1,2,3]]
 
import sys
numbers = [1, 2, 3, 4, 5]
print(sys.getsizeof(numbers))     # ~120 bytes (overhead + 5 pointers)
 
# Vs numpy array (true array)
if np is not None:
    np_arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)
    print(np_arr.nbytes)              # 20 bytes (5 × 4 bytes each)
else:
    print('NumPy is not installed; skipping NumPy example.')
 