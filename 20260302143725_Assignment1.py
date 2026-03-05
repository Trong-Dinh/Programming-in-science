# Function 1: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    # Added: Input validation: Make sure input is a number
    # Number can be of many types (like Decimal), so type casting covers the most number types
    try:
        float(number) # If the input is indeed a number, this will not be an error
    except:
        return "Not a number"
    
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Function 2: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    # Added: Input validation: Ensure variable rows is an integer
    if not isinstance(rows, int):
        return "Input is not an integer"
    
    shape = ""
    row = "\n" # \n ends every row
    for i in range(1, rows + 1):
        # Changed: Add a star to row progressiveley instead of building the row every time
        row = "*" + row # \n is at the end, so star must be added to the start of the row
        shape += row

    return shape.strip()  # Remove trailing newline at the end

# Function 3: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    # Added: Ensure variable rows is an integer
    if not isinstance(limit, int):
        return "Input is not an integer"
    
    result = ""
    # Changed: This uses a for loop instead of a while loop
    for num in range (1, limit + 1):
        if num % 3 == 0:
            result += "Multiple of 3"
        else:
            result += str(num)
        result += "\n" # \n is added in both cases, so adding it here without conditional avoids repetition of \n
        
    return result.strip()  # Remove trailing newline at the end

# Function 4: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    # Added: Set start to next even number if start is odd, so start is guaranteed to be even
    if start % 2 == 1:
        start += 1

    total = 0
    # Added: Increment num by 2 every time to avoid looping over odd numbers which we do not need
    for num in range(start, end + 1, 2): 
        total += num

    return total

if __name__ == "__main__":
    check_number(423)
    star_shape(9)
    count_multiples_of_3(13)
    sum_of_even_numbers(7, 99)