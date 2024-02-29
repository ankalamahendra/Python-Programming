def matrix_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize sums
    row_sums = [0] * rows
    col_sums = [0] * cols
    diagonal_sum = 0

    # Calculate sums
    for i in range(rows):
        for j in range(cols):
            row_sums[i] += matrix[i][j]
            col_sums[j] += matrix[i][j]
            if i == j:
                diagonal_sum += matrix[i][j]

    return row_sums, col_sums, diagonal_sum

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sums, col_sums, diagonal_sum = matrix_sum(matrix)

print("Row sums:", row_sums)
print("Column sums:", col_sums)
print("Diagonal sum:", diagonal_sum)
