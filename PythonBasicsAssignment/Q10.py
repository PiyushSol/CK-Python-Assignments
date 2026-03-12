# Tuple containing a list
data = (10, 20, [30, 40], 50)

print("Original tuple:", data)

# Modify the list inside the tuple
data[2][0] = 300
data[2].append(500)

print("Updated tuple:", data)