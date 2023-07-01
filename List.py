my_list = [1, 2, 3, 4, 5, 9, 0]
print("Original List:", my_list)

# Append method
my_list.append(6)
print("After append(6):", my_list)

# Insert method
my_list.insert(2, 10)
print("After insert(2, 10):", my_list)

# Remove method
my_list.remove(4)
print("After remove(4):", my_list)

# Pop method
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("After pop():", my_list)

# Extend method
new_list = [7, 8, 9]
my_list.extend(new_list)
print("After extend([7, 8, 9]):", my_list)

# Index method
index = my_list.index(3)
print("Index of 3:", index)

# Count method
count = my_list.count(5)
print("Count of 5:", count)

# Sort method
my_list.sort()
print("After sort():", my_list)

# Reverse method
my_list.reverse()
print("After reverse():", my_list)

# Clear method
my_list.clear()
print("After clear():", my_list)


print("\n")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", my_list)

# Slice from index 2 to index 6 (exclusive)
slice_1 = my_list[2:6]
print("Slice [2:6]:", slice_1)

# Slice from the beginning to index 5 (exclusive)
slice_2 = my_list[:5]
print("Slice [:5]:", slice_2)

# Slice from index 4 to the end
slice_3 = my_list[4:]
print("Slice [4:]:", slice_3)

# Slice from index -3 to index -1 (exclusive)
slice_4 = my_list[-3:-1]
print("Slice [-3:-1]:", slice_4)

# Slice with a step of 2
slice_5 = my_list[1:9:2]
print("Slice [1:9:2]:", slice_5)
