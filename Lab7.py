def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print(row)
    print()


def main():
    d1 = 6
    d2 = 8
    k = (d1 + d2) % 4 + 2
    shift = d1 - d2
    rows_keep = (d1 % 2) + 2

    matrix = [
        [5, 10, 15, 20, 25],
        [30, 35, 40, 45, 50]
    ]

    print_matrix(matrix, "Original rectangular matrix:")

    print("Dimensions:")
    print("Number of rows is", len(matrix))
    print("Number of columns is", len(matrix[0]))

    for row in matrix:
        print(row)

    last_column = [row[-1] for row in matrix]
    print("Last column:", last_column)

    first_3_cols = [row[:3] for row in matrix]
    print("All rows, first 3 columns:")
    for row in first_3_cols:
        print(row)

    chosen_row = d1 % len(matrix) # 6 % 2 = 0, so first row
    old_row = matrix[chosen_row][:]
    new_row = [value + k for value in old_row]
    matrix[chosen_row] = new_row

    start_col = d2 % 2 # 8 % 2 = 0, so first column, starting from 0 means including everything
    sliced_subarray = [row[start_col:] for row in matrix]

    print("\nChosen row index:", chosen_row)
    print("Old row:", old_row)
    print("New row:", new_row)

    print_matrix(matrix, "Matrix after row replacement:")

    print("Sliced sub-array from starting column", start_col)
    for row in sliced_subarray:
        print(row)


if __name__ == "__main__":
    main()