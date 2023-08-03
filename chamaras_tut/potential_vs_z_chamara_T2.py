# This code shall produce a graph of the potential energy per atom vs the z axis, using binning techniques.
import numpy as np
import matplotlib.pyplot as plt
from plotting import data_read, plot_all_data
labels = ["z-direction", "$PE (eV/atom)$"]
plot_all_data(data_read("T2_bin_v_pe"), 0, "z_direction (bin number)", "$PE$ (eV/atom)", "Potential Energy vs sample length", labels)
plt.grid()
plt.savefig("T2_pe_vs_bin")
#plt.show()
"""
def two_column_text_read(file_name):
    try:
        file = open(file_name)
    except OSError as error:
        print(error)
        return

    content = file.readlines()
    data = np.zeros([2, (len(content))], float)
    n = 0

    for line in content:
        elements = line.split()
        data[0, n] = float(elements[0])  # time
        data[1, n] = float(elements[1])  # etot

        n += 1

    return data


def plot_data(data_array):  # T1: include data_list for T1, data_list): #, display_graph):
    #for x, y in data_array: # T1 needs for loop
    plt.xlabel('bin')        # T1: 'time (ps)'
    plt.ylabel(r'$PE$ (eV/atom)')   # T1: r'$E$ (eV/atom)'
    plt.xlim(1, 10)                # T1: 0, 60
    plt.plot(data_array[0], data_array[1])              # T1: x, y
    #plt.scatter(x, y)
    plt.title('Average PE per bin')  # T1: 'Total_Energy vs Timesteps'
    plt.tight_layout()
    plt.show()
    #plt.legend([1.0, 0.5, 2.0, 3.0, 4.0])   # T1: comment in
    return


if __name__ == "__main__":
    ########################
    #Tutorial 2
    #print(plot_data(two_column_text_read('T2_bin_v_pe')))
"""