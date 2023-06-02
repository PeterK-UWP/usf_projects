

import numpy as np
import matplotlib.pyplot as plt
"""
This code is to plot lattices a, b, c, volume, energy, and enthalpy against pressure,
as well as plot energy v volume.
-what are the lattices where do you get them from
"""
# eos of p-v and e-v
# normal graphs of others vs pressure

#Diamond
def column_text_read(file_name):
    try:
        file = open(file_name)
    except OSError as error:
        print(error)
        return

    content = file.readlines()
    data = np.zeros([7, (len(content))], float)
    n = 0

    for line in content:
        elements = line.split()
        data[0, n] = float(elements[0])  #volume A^3/atom
        data[1, n] = float(elements[1])  #energy/2 eV/atom
        data[2, n] = float(elements[2])  #enthalpy eV/atom
        data[3, n] = float(elements[3])  #total pressure GPa
        data[4, n] = float(elements[4])  #lat a
        data[5, n] = float(elements[5])  #lat b
        data[6, n] = float(elements[6])  #lat c
        n += 1
    return data


def plot_graphs(data, display_graph):
    volume = data[0]
    energy = data[1]
    enthalpy = data[2]
    total_pressure = data[3]
    lattice_a = data[4]
    lattice_b = data[5]
    lattice_c = data[6]
    plot_list = [[volume, energy, enthalpy], [lattice_a, lattice_b, lattice_c]]
    figure, axes = plt.subplots(nrows=2, ncols=3, layout='constrained')
    for row_index, row in enumerate(plot_list):
        for column_index, column in enumerate(row):
            axes[row_index][column_index].plot(total_pressure, column)
            axes[row_index][column_index].set_xlabel('Total_pressure (Gpa)')
            axes[0][0].set_ylabel(r'$V$ (A^3/atom)')
            axes[0][0].set_title('Volume v Total_Pressure')
            axes[0][1].set_ylabel(r'$E$ (eV/atom)')
            axes[0][1].set_title('Energy v Total_Pressure')
            axes[0][2].set_ylabel(r'$H$ (eV/atom)')
            axes[0][2].set_title('Enthalpy v Total_Pressure')
            axes[1][0].set_ylabel('lattice vector a')
            axes[1][0].set_title('lattice a v Total_Pressure')
            axes[1][1].set_ylabel('lattice vector b')
            axes[1][1].set_title('lattice b v Total_Pressure')
            axes[1][2].set_ylabel('lattice vector c')
            axes[1][2].set_title('lattice c v Total_Pressure')
    # plt.tight_layout()
    if display_graph:
        plt.show()
    elif not display_graph:
        plt.savefig("t4_data_vs_total_pressure_diamond_expansion.png")
    return


#print(column_text_read('t4_data'))
print(plot_graphs(column_text_read('t4_data_expansion'), False))
# True for graph, False to save png
#Graphite
