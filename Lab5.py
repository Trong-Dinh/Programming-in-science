# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n == 1:
        return "*"
    
    middle = ("*" + " " * (n - 2) + "*\n") * (n - 2)
    square = "*" * n + "\n" + middle + "*" * n
    return square

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    row = ""
    for num in range(1, n+1):
        row += str(num)
        result += row + "\n"

    return result.strip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    sum = n*(n+1)/2
    return sum

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    for num in range(1, n+1):
        result += " " * (n - num) + "*" * (num * 2 - 1) + "\n"

    return result.rstrip()