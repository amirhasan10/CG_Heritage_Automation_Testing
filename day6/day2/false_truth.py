# Falsy values — these all become False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(""))        # False  (empty string)
print(bool(None))      # False
print(bool([]))        # False  (empty list)

# Truthy values — these all become True
print(bool(1))         # True
print(bool(-99))       # True  (any non-zero number)
print(bool("hi"))      # True  (non-empty string)
print(bool(" "))       # True  (even a space!)

# Real-world: Validate user input
username = input("Enter username: ")  # try entering nothing
if bool(username):                     # same as: if username:
    print(f"Welcome, {username}!")
else:
    print("Username cannot be empty!")