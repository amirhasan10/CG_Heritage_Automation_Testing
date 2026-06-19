name  = "Kavitha"
score = 92

# Old way — confusing and error-prone
print("Hello %s, you scored %d marks" % (name, score))

# .format() way — verbose
print("Hello {}, you scored {} marks".format(name, score))

# ✅ f-string way — clean, readable, fast
print(f"Hello {name}, you scored {score} marks")