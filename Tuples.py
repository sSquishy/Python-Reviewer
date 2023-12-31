# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Accessing elements in a tuple
print("First fruit:", fruits[0])  # Prints the first element (index 0)
print("Second fruit:", fruits[1])  # Prints the second element (index 1)
print("Last fruit:", fruits[-1])  # Prints the last element (index -1)

# Attempting to modify a tuple will result in an error
# fruits[0] = "orange"  # This will raise a TypeError

# Iterating through a tuple
print("All fruits:")
for fruit in fruits:
    print(fruit)

# Checking if an item exists in the tuple
if "banana" in fruits:
    print("Yes, banana is in the tuple")
else:
    print("No, banana is not in the tuple")

# Getting the length of a tuple
num_fruits = len(fruits)
print("Number of fruits in the tuple:", num_fruits)

# Combining tuples (creating a new tuple)
more_fruits = ("grape", "kiwi", "orange")
combined_fruits = fruits + more_fruits
print("Combined fruits:", combined_fruits)

# Counting the occurrences of an item in a tuple
count_apple = combined_fruits.count("apple")
print("Number of apples in the combined fruits:", count_apple)

# Finding the index of an item in a tuple
index_cherry = combined_fruits.index("cherry")
print("Index of 'cherry' in the combined fruits:", index_cherry)

# Unpacking a tuple
a, b, c = fruits
print("Unpacked fruits:", a, b, c)