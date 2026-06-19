# float → int  (decimal is TRUNCATED, not rounded)
price = 99.99
print(int(price))          # 99  (not 100!)

# str → int  (string must contain only digits)
age_input = "25"            # from user input — always a string
age = int(age_input)
print(age + 5)             # 30  (now we can do math)

# bool → int
print(int(True))           # 1
print(int(False))          # 0

# Real-world: ATM withdrawal
balance_str = "15000"      # imagine reading from a file
withdrawal  = 3500
new_balance = int(balance_str) - withdrawal
print(f"Remaining balance: ₹{new_balance}")

# ❌ This will crash — cannot convert non-numeric string
# int("hello")   → ValueError
# int("12.5")    → ValueError (use float() first)