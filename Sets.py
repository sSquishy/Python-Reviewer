# Creating sets
fruits = {"apple", "banana", "cherry"}
colors = {"red", "green", "blue"}

# Printing the sets
print("Fruits Set:", fruits)
print("Colors Set:", colors)

# Adding an element to a set
fruits.add("orange")
print("Fruits Set after adding 'orange':", fruits)

# Removing an element from a set
fruits.remove("banana")
print("Fruits Set after removing 'banana':", fruits)

# Checking if an element is in a set
if "apple" in fruits:
    print("'apple' is in the Fruits Set")
else:
    print("'apple' is not in the Fruits Set")

# Combining sets (Union)
combined_set = fruits.union(colors)
print("Combined Set (Union of Fruits and Colors):", combined_set)

# Finding the common elements between sets (Intersection)
common_elements = fruits.intersection(colors)
print("Common Elements between Fruits and Colors:", common_elements)

# Checking if one set is a subset of another
is_subset = {"red", "green"}.issubset(colors)
print("Is {'red', 'green'} a subset of Colors?", is_subset)

# Checking if two sets have no common elements (Disjoint sets)
are_disjoint = fruits.isdisjoint(colors)
print("Are Fruits and Colors disjoint sets?", are_disjoint)

# Removing all elements from a set
fruits.clear()
print("Fruits Set after clearing:", fruits)