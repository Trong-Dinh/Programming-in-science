# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    end_height = h0 - 4.9 * t ** 2 # 9.8 / 2 = 4.9
    return end_height

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    speed = 20 # Constant
    distance = speed * t
    return distance

# First question
def prompt_ball():
    initial_height = float(input("Enter initial height: "))
    time = float(input("Enter time: "))
    # Check if time is positive; if negative, do not continue
    if time < 0:
        print(f"Invalid time: {time}")
        return
    
    final_height = calculate_height(initial_height, time)

    # Make "second" singular when time is equal to 1 second
    if time == 1:
        plural = ""
    else:
        plural = "s"    
    
    print(f"Height of the ball at time {time} second{plural} = {final_height} meters")

# Second question
def prompt_car():
    time = float(input("Enter time for car (in seconds): "))
    # Check if time is positive; if negative, do not continue
    if time < 0:
        print(f"Invalid time: {time}")
        return
    
    distance = calculate_car_distance(time)

    # Make "second" singular when time is equal to 1 second
    if time == 1:
        plural = ""
    else:
        plural = "s"

    print(f"The car will travel {distance} meters in {time} second{plural}.")

if __name__ == "__main__":
    prompt_ball() # The two questions were converted into functions so both can have variable "time" in their respective scope
    print("") # Print a blank line between the two parts of the program
    prompt_car()