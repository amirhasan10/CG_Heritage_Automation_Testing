# Bank Deposit System
balance      = float(input("Current Balance (₹): "))
deposit_amt  = float(input("Deposit Amount  (₹): "))

new_balance  = balance + deposit_amt
print(f"Updated Balance: ₹{new_balance:.2f}")

# Output:
# Current Balance (₹): 15000
# Deposit Amount  (₹): 5500.50
# Updated Balance: ₹20500.50