import numpy as np
import matplotlib.pyplot as plt
"""
this code read t2 data outputs the energy change between each ionic step, calculates the enthalpy from H = U + PV
and then plots 6 graphs: energy, enthalpy, pressure, xx pressure, yy pressure, and zz pressure against each
ionic step
"""


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
        data[0, n] = float(elements[0])
        data[1, n] = float(elements[1])
        data[2, n] = float(elements[2])
        data[3, n] = float(elements[3])
        data[4, n] = float(elements[4])
        data[5, n] = float(elements[5])
        data[6, n] = float(elements[6])
        n += 1
    return data


def energy_change(data):
    change_list = []
    for i in np.linspace(0, len(data[1])-1, 5):   # (0, ionic step - 1, ionic step)
        if i < 4:   # ionic step - 1
            change = data[1][int(i+1)] - data[1][int(i)]
            change_list.append(change)
        if i == 4:  # ionic step
            continue
    return change_list


def enthalpy(data):
    energy = np.array(data[1])  # eV
    pressure = np.array(data[2])*10**8  # Pa
    volume = np.array(data[3])*10**-30  # m^3
    enthalpy_array = energy + (pressure * volume) * 6.242*10**18  # eV
    return enthalpy_array / 2  # eV / atom


def plot_data(data, enthalpy_data, display_graph):
    ionic_step_data = data[0]
    energy_data = data[1]
    pressure_data = data[2]*0.1
    xx_data = data[4]*0.1
    yy_data = data[5]*0.1
    zz_data = data[6]*0.1
    plot_list = [[energy_data, enthalpy_data, pressure_data], [xx_data, yy_data, zz_data]]
    figure, axes = plt.subplots(nrows=2, ncols=3, layout='constrained')
    for row_index, row in enumerate(plot_list):
        for column_index, column in enumerate(row):
            axes[row_index][column_index].plot(ionic_step_data, column)
            axes[row_index][column_index].set_xlabel('Ionic Step')
            axes[0][0].set_ylabel(r'$E$ (eV/atom)')
            axes[0][0].set_title('Energy per Ionic Step')
            axes[0][1].set_ylabel(r'$H$ (eV)')
            axes[0][1].set_title('Enthalpy per Ionic Step')
            axes[0][2].set_ylabel(r'$P$ (Pa)')
            axes[0][2].set_title('Pressure/Ionic Step')
            axes[1][0].set_ylabel(r'$P_{xx}$ (GPa)')
            axes[1][0].set_title('XX Pressure per Ionic Step')
            axes[1][1].set_ylabel(r'$P_{yy}$ (GPa)')
            axes[1][1].set_title('YY Pressure/Ionic Step')
            axes[1][2].set_ylabel(r'$P_{zz}$ (GPa)')
            axes[1][2].set_title('ZZ Pressure/Ionic Step')
    #plt.tight_layout()
    if display_graph:
        plt.show()
    elif not display_graph:
        plt.savefig("t2_data_vs_ionic_step.png")
    return


#print(column_text_read('t2_data'))
#print(energy_change(column_text_read('t2_data')))
print(enthalpy(column_text_read('t2_data')))
print(plot_data(column_text_read('t2_data'), enthalpy(column_text_read('t2_data')), False))  # True for graph, False to save png