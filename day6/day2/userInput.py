# Simulating messy user input
raw_username = "   admin   "
raw_pin      = "  1234  "

print(len(raw_username))               # 10 (with spaces)
print(len(raw_username.strip()))       # 5  (clean)

clean_username = raw_username.strip()  # removes both sides
print(f"[{clean_username}]")           # [admin]

# lstrip — only left side
text = "   left-spaces-only   "
print(f"[{text.lstrip()}]")            # [left-spaces-only   ]

# rstrip — only right side
print(f"[{text.rstrip()}]")            # [   left-spaces-only]

# strip specific characters
price_str = "₹₹₹250.00₹₹"
print(price_str.strip("₹"))            # 250.00

# Real-world: Login validation
stored_password = "secret123"
entered_password = "  secret123  "     # user accidentally added spaces
print(entered_password.strip() == stored_password)  # True  ✅