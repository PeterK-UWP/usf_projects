import numpy as np
import matplotlib.pyplot as plt
"""
This code reads t0 data and outputs the energy per atom against the scf steps
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
        data[0, n] = float(elements[0])
        data[1, n] = float(elements[1])
        n += 1

    return data


def plot_data(data, display_graph):
    x_data = data[0]
    plt.xlabel('scf step')
    y_data = data[1]
    plt.ylabel(r'$E$ (eV/atom)')
    plt.plot(x_data, y_data)
    plt.tight_layout()
    if display_graph:
        plt.show()
    elif not display_graph:
        plt.savefig("t0_energy_vs_scf_step.png")
    return

print(two_column_text_read('t0_data'))
print(plot_data(two_column_text_read('t0_data'), True))  # True for graph, False to save png
