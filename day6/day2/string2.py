# Why str() matters
name  = "Deepa"
score = 95

# ❌ This crashes: cannot concatenate str and int
# print("Score: " + score)  → TypeError

# ✅ Convert first
print("Score: " + str(score))    # Score: 95

# More conversions
print(str(3.14))               # '3.14'
print(str(True))               # 'True'
print(str(None))               # 'None'

# Real-world: Building a receipt
item     = "Notebook"
qty      = 3
price    = 45.0
receipt  = item + " x" + str(qty) + " = ₹" + str(qty * price)
print(receipt)                 # Notebook x3 = ₹135.0

# Better way with f-strings (Section 5)
receipt2 = f"{item} x{qty} = ₹{qty * price}"
print(receipt2)                # Notebook x3 = ₹135.0