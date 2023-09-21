# Example 1: Basic if-else statement
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# Example 2: Nested if-else statements
y = 7
if y > 10:
    print("y is greater than 10")
else:
    if y > 5:
        print("y is greater than 5 but not greater than 10")
    else:
        print("y is not greater than 5")

# Example 3: Elif (else if) statement
z = 3
if z > 5:
    print("z is greater than 5")
elif z == 5:
    print("z is equal to 5")
else:
    print("z is less than 5")

# Example 4: Ternary conditional expression
a = 15
b = 10
max_value = a if a > b else b
print("The maximum value between a and b is:", max_value)

# Example 5: Using multiple conditions
grade = 85
if grade >= 90:
    print("A grade")
elif grade >= 80:
    print("B grade")
elif grade >= 70:
    print("C grade")
elif grade >= 60:
    print("D grade")
else:
    print("F grade")

# Example 6: Checking for empty or None
value = None
if value is None:
    print("Value is None")
elif not value:
    print("Value is empty")
else:
    print("Value has a value")

# Example 7: Short-circuiting with logical operators
income = 50000
credit_score = 700
if income >= 50000 and credit_score >= 700:
    print("You qualify for a loan")
else:
    print("You do not qualify for a loan")