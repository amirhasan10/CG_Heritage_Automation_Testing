# Direct boolean assignment
is_raining    = False
has_umbrella  = True
account_active = True

# Booleans from comparisons
age = 17
can_vote = age >= 18          # False
can_drive = age >= 16         # True (in some states)

print(can_vote)               # False
print(can_drive)              # True
print(type(can_vote))         # <class 'bool'>

# Boolean in a real decision
balance = 5000
amount  = 3000
can_withdraw = balance >= amount
print("Withdrawal allowed:", can_withdraw)  # True

# Booleans are secretly 1 and 0
print(True + True)   # 2
print(False * 100)   # 0
print(int(True))     # 1