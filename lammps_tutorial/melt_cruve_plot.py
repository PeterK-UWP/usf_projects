# temp*000 txt files contain: time temp energy press
import numpy as np
import matplotlib.pyplot as plt


def four_column_text_read(file_name):
    try:
        file = open(file_name)
    except OSError as error:
        print(error)
        return

    content = file.readlines()
    data = np.zeros([5, (len(content))], float)
    n = 0

    for line in content:
        elements = line.split()
        data[0, n] = float(elements[0])  # time
        data[1, n] = float(elements[1])  # temp
        data[2, n] = float(elements[2])  # PE
        data[3, n] = float(elements[3])  # press
        data[4, n] = float(elements[4])  # V

        n += 1

    return data  # time temp energy press


def temp_time(data):
    plt.plot(data[0], data[1])
    plt.scatter(data[0], data[1])
    plt.title("Temperature vs Time for T_0 = 6500K")
    plt.xlabel("Time (picoseconds)")
    plt.ylabel("Temp (K)")
    plt.savefig("6500 Temp vs Time")
    plt.show()
    return


def pot_energy_time(data):
    plt.plot(data[0], data[2])
    plt.scatter(data[0], data[2])
    plt.title("Potential Energy vs Time for T_0 = 6500K")
    plt.xlabel("Time (picoseconds)")
    plt.ylabel("Potential Energy (eV)")
    plt.savefig("6500 PE vs Time")
    plt.show()


def pressure_time(data):
    plt.plot(data[0], data[3])
    plt.scatter(data[0], data[3])
    plt.title("Pressure vs Time for T_0 = 6500K")
    plt.xlabel("Time (picoseconds)")
    plt.ylabel("Pressure (GPa)")
    plt.savefig("6500 Pressure vs Time")
    plt.show()


def vol_time(data):
    plt.plot(data[0], data[4])
    plt.scatter(data[0], data[4])
    plt.title("Volume vs Time for T_0 = 6500K")
    plt.xlabel("Time (picoseconds)")
    plt.ylabel("Volume (A^3)")
    plt.savefig("6500 Volume vs Time")
    plt.show()


def temp_avg(data):
    avg_temp = sum(data[1])/float(len(data[1]))
    return avg_temp


if __name__ == "__main__":
    print(temp_time(four_column_text_read("temp6500")))
    print(pot_energy_time(four_column_text_read("temp6500")))
    print(pressure_time(four_column_text_read("temp6500")))
    print(vol_time(four_column_text_read("temp6500")))

    print(temp_avg(four_column_text_read("temp6500")))

"""
6000 + 7000 / 2 = 6500 delta T = 325K ->  average -> 6465.365
6000 + 6465.365 / 2 = 6232.6825  delta T = 311K -> average -> 6271.344
6000 + 6271.344 / 2 = 6135.5  delta T = 305   This is good enough.


"""