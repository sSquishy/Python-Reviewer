# Function without parameters
def greet():
    print("Hello, welcome!")

greet()  # Call the function

# Function with parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print("Sum:", result)

# Function with default argument
def multiply_numbers(a, b=2):
    return a * b

result = multiply_numbers(5)
print("Product:", result)

# Function that returns multiple values
def calculate_values(a, b):
    sum_result = a + b
    difference = a - b
    return sum_result, difference

sum_result, difference = calculate_values(10, 5)
print("Sum:", sum_result)
print("Difference:", difference)

#local/global vairables
print("\n")
def my_function():
    local_variable = 10
    print("Local variable:", local_variable)

my_function()  # Output: Local variable: 10

global_variable = 20

def another_function():
    global global_variable
    global_variable += 5
    print("Global variable:", global_variable)

another_function()  # Output: Global variable: 25
