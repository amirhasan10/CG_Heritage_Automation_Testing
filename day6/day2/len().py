name    = "Ananya"
message = "Hello, World!"
empty   = ""

print(len(name))      # 6
print(len(message))   # 13  (space and ! are counted)
print(len(empty))     # 0

# Real-world: Password strength validator
password = "myPass@123"
min_length = 8

if len(password) >= min_length:
    print(f"Password length OK ({len(password)} characters)")
else:
    print(f"Too short! Need {min_length - len(password)} more character(s)")

# Twitter-style character counter
tweet = "Python is amazing for data science and automation!"
remaining = 280 - len(tweet)
print(f"{len(tweet)}/280 characters used, {remaining} remaining")