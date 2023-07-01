print("Types of Data using type('data type')\n")
# Integer
num = 10
print("Integer:", num, "Type:", type(num))

# Float
pi = 3.14
print("Float:", pi, "Type:", type(pi))

# String
name = "John Doe"
print("String:", name, "Type:", type(name))

# Boolean
is_true = True
print("Boolean:", is_true, "Type:", type(is_true))

# List
numbers = [1, 2, 3, 4, 5]
print("List:", numbers, "Type:", type(numbers))

# Tuple
coordinates = (10, 20)
print("Tuple:", coordinates, "Type:", type(coordinates))


print("\n\nData type conversion")
# Explicit data type conversion using the str() function
num1 = 10
str_num1 = str(num1)  # Explicitly converting num1 to a string
print("\nExplicit conversion - num1:", str_num1, "Type:", type(str_num1))

# Implicit data type conversion during string concatenation
num2 = 5
str_num2 = "The value of num2 is: " + str(num2)  # Implicitly converting num2 to a string
print("Implicit conversion - str_num2:", str_num2, "Type:", type(str_num2))

# Explicit data type conversion using the int() function
num3 = "15"
int_num3 = int(num3)  # Explicitly converting num3 to an integer
print("Explicit conversion - int_num3:", int_num3, "Type:", type(int_num3))

# Implicit data type conversion during arithmetic operation
num4 = "20"
result = int(num4) + 5  # Implicitly converting num4 to an integer during addition
print("Implicit conversion - result:", result, "Type:", type(result))
