#Teacher sample file 1
#Filename: oscillatory_2672601.csv
#This uses 5 + d2 = 5 rows since d2 = 0.
#Teacher sample file 2
#Filename: standing_2672601.csv
#This uses 4 + rows_keep = 7 rows since rows_keep = 3.
from os import path
import numpy as np
import math

d1 = 6
d2 = 8
k = (d1 + d2) % 4 + 2
shift = d1 - d2
rows_keep = (d1 % 2) + 2

def read_oscillatory_wave_data(filename):
    data = np.genfromtxt(filename, delimiter=",", skip_header=1)
 
    #data = np.loadtxt(filename, delimiter=',')  # Assuming CSV format
    lengths = data[:, 0]
    amplitudes = data[:, 1]
    mean_amp = np.mean(amplitudes)
    max_amp = np.max(amplitudes)
    return lengths, amplitudes, mean_amp, max_amp


def read_standing_wave_data(filename):
    data = np.genfromtxt(filename, delimiter=",", skip_header=1)
    lengths = data[:, 0]
    tensions = data[:, 1]
    speeds = np.sqrt(tensions / 1)
    return lengths, tensions, speeds


def main():
    osc_file = "oscillatory_2672601.csv"
    stand_file = "standing_2672601.csv"
 

    lengths1, amplitudes, mean_amp, max_amp = read_oscillatory_wave_data(osc_file)

    print("\nOriginal lengths:", lengths1)
    print("Original oscillatory amplitudes:", amplitudes)
    print("Original mean amplitude:", mean_amp)
    print("Original max amplitude:", max_amp)

    new_amplitudes = amplitudes[:5+d2] + shift # Only create the first 5+d2 rows
    new_mean_amp = np.mean(new_amplitudes)
    new_max_amp = np.max(new_amplitudes)

    print("\nShifted amplitudes:", new_amplitudes)
    print("New mean amplitude:", new_mean_amp)
    print("New max amplitude:", new_max_amp)

    lengths2, tensions, speeds = read_standing_wave_data(stand_file)

    print("\nOriginal lengths:", lengths2)
    print("Original tensions:", tensions)
    print("Original wave speeds:", speeds)

    new_tensions = tensions[:4+rows_keep] * k # Only create the first 4+rows_keep rows
    new_speeds = np.sqrt(new_tensions / 1)

    print("\nScaled tensions:", new_tensions)
    print("New wave speeds:", new_speeds)

    print("\nManual oscillatory check using first 3 amplitudes:")
    print("Original first 3 amplitudes:", amplitudes[:3])
    print("Shifted first 3 amplitudes:", new_amplitudes[:3])

    print("\nManual standing-wave check using first row:")
    print("First tension =", tensions[0])
    print("Scaled first tension =", new_tensions[0])
    print("First new speed =", math.sqrt(new_tensions[0]))


if __name__ == "__main__":
    main()
