def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table

# Get user input for the table size
size = int(input("Enter the size of the multiplication table: "))

# Generate the multiplication table
table = multiplication_table(size)

# Print the multiplication table
for row in table:
    print(row)
