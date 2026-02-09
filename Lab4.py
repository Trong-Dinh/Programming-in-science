# Function 1: Check if the given number is a proper day number and return "It is a Weekday!" if it is, or "It is a Weekend!" if it is not.
def check_weekday_or_weekend(day_number):
    if day_number <= 0 or day_number >= 8:
        return "Not a proper day number!"
    
    if day_number == 6 or day_number == 7:
        return "It is a Weekend!"
    
    return "It is a Weekday!"

# Function 2: Check if the given number is a proper day number and return the corresponding day name.
def get_day_name(day_number):
    if day_number <= 0 or day_number >= 8:
        return "Not a proper day number!"
    
    if day_number == 1:
        day_name = "Monday"
    elif day_number == 2:
        day_name = "Tuesday"
    elif day_number == 3:
        day_name = "Wednesday"
    elif day_number == 4:
        day_name = "Thursday"
    elif day_number == 5:
        day_name = "Friday"
    elif day_number == 6:
        day_name = "Saturday"
    elif day_number == 7:
        day_name = "Sunday"

    return f"It is a {day_name}!"
    