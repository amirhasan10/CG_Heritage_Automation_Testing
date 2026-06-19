# Real-life floats
item_price  = 249.99       # product price
gst_rate    = 0.18         # 18% GST
temperature = 37.5         # body temperature in °C
latitude    = 22.5726      # latitude of Kolkata

print(type(item_price))    # <class 'float'>

# Calculate GST
gst_amount  = item_price * gst_rate
total_bill  = item_price + gst_amount
print(f"Item: ₹{item_price}  |  GST: ₹{gst_amount:.2f}  |  Total: ₹{total_bill:.2f}")

# Float precision gotcha
print(0.1 + 0.2)           # 0.30000000000000004  (floating point!))
print(round(0.1 + 0.2, 2)) # 0.3  (use round() to fix it)