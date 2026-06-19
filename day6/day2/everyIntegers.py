# Everyday integers
population = 1_380_000_000   # India's population (underscores for readability)
floor_number = -2            # negative integer (basement floor)
items_in_cart = 0

print(type(population))      # <class 'int'>
print(type(floor_number))    # <class 'int'>

# Integer arithmetic
total_price = 450
discount    = 50
final_price = total_price - discount
print("Final price: ₹", final_price)

# Integer division and modulo
apples = 17
children = 5
each_gets = apples // children   # floor division → 3
leftover  = apples % children    # remainder → 2
print(f"Each child gets {each_gets} apples, {leftover} left over")