sentence = "I love Java. Java is great."
updated  = sentence.replace("Java", "Python")
print(updated)    # I love Python. Python is great.

# Replace only first occurrence
partial  = sentence.replace("Java", "Python", 1)
print(partial)    # I love Python. Java is great.

# Real-world: Template personalisation
template = "Dear CUSTOMER_NAME, your order ORDER_ID is ready."
msg = template.replace("CUSTOMER_NAME", "Ravi").replace("ORDER_ID", "#78234")
print(msg)