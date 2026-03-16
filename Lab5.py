def main():
    d1 = 6
    d2 = 8
    k = (d1 + d2) % 4 + 2
    shift = d1 - d2
    rows_keep = (d1 % 2) + 2

    n = int(input("How many readings? "))

    # Get input number n times
    readings = [float(input("Enter reading: ")) for i in range(n)]

    # Full list
    print("Full list:", readings)

    if len(readings) > 0:
        print("First reading:", readings[0])
        print("Last reading:", readings[-1])
    else:
        print("The list is empty.")

    if len(readings) >= 4:
        print("Slice from index 1 to index 3:", readings[1:4])
    else:
        print("Not enough values for slice [1:4].")

    total = sum(readings)
    print("Sum of readings:", total)

    # Component B
    shifted = [x + shift for x in readings]
    scaled = [x * k for x in readings]
    zipped_sum = [a + b for a, b in zip(readings, shifted)]

    print("Shifted readings:", shifted)
    print("Scaled readings:", scaled)
    print("Element-wise sum of original and shifted:", zipped_sum)


if __name__ == "__main__":
    main()