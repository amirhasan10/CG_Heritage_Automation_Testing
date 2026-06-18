cart = ['apple', 'banana', 'cherry', 'dates', 'elderberry']
# 0 1 2 3 4
# -5 -4 -3 -2 -1
print(cart[0]) # apple → first item
print(cart[2]) # cherry → third item
print(cart[-1]) # elderberry → last item
print(cart[-2]) # dates → second from last
# Nested list access
students = [['Alice', 90], ['Bob', 85], ['Carol', 95]]
print(students[0][0]) # Alice
print(students[2][1]) # 95

# Reverse the list
print(scores[::-1]) # [100, 95, 90, 85, 78, 70, 62, 55]
# Negative slicing
print(scores[-3:]) # [95, 100] ... wait:
print(scores[-3:]) # [90, 95, 100] → last 3 items