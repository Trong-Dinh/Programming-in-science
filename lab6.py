matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]

def main():    
    d1 = 6
    d2 = 8
    k = (d1 + d2) % 4 + 2
    shift = d1 - d2
    rows_keep = (d1 % 2) + 2

    # full matrix
    print("Full matrix:", matrix)

    # One element (2nd row and 3rd column)
    print("One element:", matrix[1][2])

    # First two rows
    print("First two rows:", matrix[:2])

    # First column
    print("First column:", [row[0] for row in  matrix])

    # 2x2 Subarray from upper left corner
    print("Subarray:", [row[:2] for row in matrix[:2]])

    # Before modification
    print("Original matrix:", matrix)
    chosen_row = d1 % len(matrix)
    old_row = matrix[chosen_row][:]
    new_row = [value + shift for value in old_row]
    matrix[chosen_row] = new_row

    print("\nChosen row index:", chosen_row)
    print("Old row:", old_row)
    print("New row:", new_row)

    print("Matrix after row replacement:", matrix)

    start_col = d2 % 4
    print("Chosen column index:", start_col)

    for row in matrix:
        row[start_col] *= k

    print("Matrix after column change:", matrix)

    sliced_subarray = [row[:k] for row in matrix[:rows_keep]]

    print("Sliced sub-array until column", k, "and until row", rows_keep, ":")
    print(sliced_subarray)

    print("Modified matrix:", matrix)

if __name__ == "__main__":
    main()