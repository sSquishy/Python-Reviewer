# Conditional statements example
x = 10
y = 5

# if statement
if x > y:
    print("x is greater than y")

# if-else statement
if x < y:
    print("x is less than y")
else:
    print("x is greater than or equal to y")

# if-elif-else statement
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# nested if statement
if x > 0:
    if y > 0:
        print("Both x and y are positive")

# short-circuiting with logical operators
if x > 0 and y > 0:
    print("Both x and y are positive")
