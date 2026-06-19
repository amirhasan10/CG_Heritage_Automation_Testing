email = "user.name@gmail.com"

# find() — returns index of first match, -1 if not found
print(email.find("@"))         # 9
print(email.find("yahoo"))     # -1  (not found)

# count() — how many times does a substring appear?
text = "banana"
print(text.count("a"))         # 3

# startswith() / endswith() — check prefixes/suffixes
filename = "report_2024.pdf"
print(filename.endswith(".pdf"))    # True
print(filename.startswith("report")) # True

# Real-world: Validate email format
def is_valid_email(e):
    return "@" in e and e.endswith(".com") or e.endswith(".in")

print(is_valid_email("test@gmail.com"))   # True
print(is_valid_email("notanemail"))        # False