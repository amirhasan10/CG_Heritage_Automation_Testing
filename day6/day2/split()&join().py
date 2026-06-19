# split() — breaks string into a list
csv_row  = "Arjun,25,Mumbai,Engineer"
fields   = csv_row.split(",")
print(fields)          # ['Arjun', '25', 'Mumbai', 'Engineer']
print(fields[0])       # Arjun
print(fields[2])       # Mumbai

# split on whitespace by default
sentence = "Python is fun to learn"
words    = sentence.split()
print(words)           # ['Python', 'is', 'fun', 'to', 'learn']
print(len(words))      # 5

# join() — reassembles a list back into a string
tags = ["python", "coding", "beginner", "tutorial"]
hashtags = "#" + "  #".join(tags)
print(hashtags)        # #python  #coding  #beginner  #tutorial