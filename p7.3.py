# Fill matrix
quantity = [
    [2, 4, 3, 6, 9],
    [5, 8, 9, 3, 7],
    [1, 4, 3, 2, 10]
]

# Reverse a specific row in the matrix
def reverse(matrix, rows, cols, row_number):
    if row_number < 0 or row_number >= rows:
        print("Invalid row number")
        return
    # Reverse the row
    matrix[row_number] = matrix[row_number][::-1]

# Print before reversing
print("Matrix before reversing row 1:")
for row in quantity:
    print(row)

# Call the function to reverse row 1
reverse(quantity, 3, 5, 1)

# Print matrix after reversing
print("\nMatrix after reversing row 1:")
for row in quantity:
    print(row)
