# Use cases for None
# 1. Placeholder before a value is known
winner = None                 # competition hasn't started
print(winner)                 # None
print(type(winner))           # <class 'NoneType'>

# 2. Function that returns nothing returns None implicitly
def greet(name):
    print(f"Hello, {name}!")

result = greet("Amit")        # prints Hello, Amit!
print(result)                 # None

# 3. Checking for None — use 'is', not '=='
score = None
if score is None:
    print("Score not submitted yet")
else:
    print(f"Your score: {score}")