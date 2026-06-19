employees = ['Alice', 'Bob', 'Carol']
# New employee joins
employees.append('David')
employees.append('Eva')
print(employees)
# ['Alice', 'Bob', 'Carol', 'David', 'Eva']
# append() adds ONE item at a time
# To add multiple items, use extend()
employees.extend(['Frank', 'Grace'])
print(employees)
# ['Alice', 'Bob', 'Carol', 'David', 'Eva', 'Frank', 'Grace']

tasks = ['Write report', 'Send email', 'Attend meeting']
# Urgent task needs to be first
tasks.insert(0, 'Fix critical bug') # insert at index 0
print(tasks)
# ['Fix critical bug', 'Write report', 'Send email', 'Attend meeting']
# Insert in the middle
tasks.insert(2, 'Code review') # at index 2
print(tasks)
# ['Fix critical bug', 'Write report', 'Code review', 'Send email', 'Attend meeting']