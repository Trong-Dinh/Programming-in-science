
# Function : Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    # Set only keeps unique values
    numbers_set = set(numbers)
    sorted_list = list(sorted(numbers_set))
    return sorted_list

# Function : Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    sums = []
    sum = 0
    for num in arr:
        sum += num
        sums.append(sum)

    return sums

# Function : Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    sliced = [lst[i] for i in range(0, len(lst)-1, step)]
    return sliced

# Function : Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    dot_product = 0
    for num1, num2 in zip(list1, list2):
        dot_product += num1 * num2
    
    return dot_product

# Function : Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    # Initialize matrix with zeroes
    end_matrix = [[0 for i in range(len(matrix1))] for j in range(len(matrix2))]

    # Compute "dot product" for index i, j of the resulting matrix
    # i is the row
    for i in range(len(matrix1)):
        # j is the column
        for j in range(len(matrix2)):
            # Find "dot product of column and row of each "vector"
            vec1 = matrix1[i]
            vec2 = [row[j] for row in matrix2]

            product = 0
            for num1, num2 in zip(vec1, vec2):
                product += num1 * num2

            end_matrix[i][j] = dot_product

    return end_matrix