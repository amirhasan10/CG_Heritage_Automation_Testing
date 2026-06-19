# Different ways to create strings
first_name    = 'Priya'
last_name     = "Patel"
address       = """123, MG Road,
Bengaluru - 560001"""

# Strings with special characters
message       = "He said, \"Hello!\""   # escaped quotes
file_path     = "C:\\Users\\Priya"       # escaped backslash
new_line_demo = "Line1\nLine2"            # \n = newline

# String operations
full_name = first_name + " " + last_name  # concatenation
repeated  = "Ha" * 3                       # repetition

print(full_name)                           # Priya Patel
print(repeated)                            # HaHaHa
print(len(full_name))                      # 10 (characters including space)
print(type(full_name))                     # <class 'str'>