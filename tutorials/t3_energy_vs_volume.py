import numpy as np
import matplotlib.pyplot as plt


def column_text_read(file_name):
    try:
        file = open(file_name)
    except OSError as error:
        print(error)
        return

    content = file.readlines()
    data = np.zeros([9, (len(content))], float)
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
        data[7, n] = float(elements[7])
        data[8, n] = float(elements[8])
        n += 1
    return data


def energy_change(data):
    change_list = []
    for i in np.linspace(0, len(data[1])-1, 12):   # (0, ionic step - 1, ionic step)
        if i < 11:   # ionic step - 1
            change = data[1][int(i+1)] - data[1][int(i)]
            change_list.append(change)
        if i == 11:  # ionic step
            continue
    return change_list


def enthalpy_check(data):  # units dont match
    energy = np.array(data[1])
    pressure = np.array(data[2])
    volume = np.array(data[3])
    theoretical_enthalpy_array = energy + pressure * volume
    calculated_enthalpy = data[8]
    return theoretical_enthalpy_array, calculated_enthalpy


def plot_data(data, display_graph):
    ionic_step_data = data[0]
    energy_data = data[1]
    pressure_data = data[2]
    volume_data = data[4]
    xx_data = data[5]
    yy_data = data[6]
    zz_data = data[7]
    enthalpy_data = data[8]
    plot_list_step = [[energy_data, enthalpy_data, pressure_data, volume_data, enthalpy_data],
                      [xx_data, yy_data, zz_data, energy_data, pressure_data]]
    plot_list_volume = [energy_data, enthalpy_data, pressure_data]
    figure, axes = plt.subplots(nrows=2, ncols=5, layout='constrained')
    for row_index, row in enumerate(plot_list_step):
        for column_index, column in enumerate(row):


            axes[row_index][column_index].plot(ionic_step_data, column)  # setting x axis, go across first then next line
            axes[row_index][column_index].set_xlabel('Ionic Step')
            axes[0][0].set_ylabel(r'$E$ (eV/atom)')
            axes[0][0].set_title('Energy per Ionic Step')
            axes[0][1].set_ylabel(r'$H$ (eV)')
            axes[0][1].set_title('Enthalpy per Ionic Step')
            axes[0][2].set_ylabel(r'$P$ (kB)')
            axes[0][2].set_title('Pressure/Ionic Step')
            axes[0][3].set_ylabel(r'$V$ ($A$)')
            axes[0][3].set_title('Volume/Ionic Step')
            axes[1][0].set_ylabel(r'$P_{xx}$ (kB)')
            axes[1][0].set_title('XX Pressure per Ionic Step')
            axes[1][1].set_ylabel(r'$P_{yy}$ (kB)')
            axes[1][1].set_title('YY Pressure/Ionic Step')
            axes[1][2].set_ylabel(r'$P_{zz}$ (kB)')
            axes[1][2].set_title('ZZ Pressure/Ionic Step')

            axes[0][4].plot(volume_data,enthalpy_data)  # setting x axis
            axes[0][4].set_xlabel('$V$ $A$/atom')
            axes[1][3].plot(volume_data, energy_data)  # setting x axis
            axes[1][3].set_xlabel('$V$ $A$/atom')
            axes[1][4].plot(volume_data, pressure_data)  # setting x axis
            axes[1][4].set_xlabel('$V$ $A$/atom')

            axes[0][4].set_ylabel(r'$H$ (eV)')
            axes[0][4].set_title('Enthalpy per Volume')
            axes[1][3].set_ylabel(r'$E$ (eV)')
            axes[1][3].set_title('Energy per Volume')
            axes[1][4].set_ylabel(r'$P$ (kB)')
            axes[1][4].set_title('Pressure per Volume')

            """
    for row_index, row in enumerate(plot_list_volume):
        axes[row_index].plot(volume_data, row)
        axes.set_xlabel('$V$ $A$/atom')
        axes[0][4].set_ylabel(r'$H$ (eV)')
        axes[0][4].set_title('Enthalpy per Volume')
        axes[1][3].set_ylabel(r'$E$ (eV)')
        axes[1][3].set_title('Energy per Volume')
        axes[1][4].set_ylabel(r'$P$ (kB)')
        axes[1][4].set_title('Pressure per Volume')
        ~~
        for column in enumerate(row):
            
            axes[row_index1][column_index1].plot(volume_data, column1)  # setting x axis
            axes[row_index1][column_index1].set_xlabel('$V$ $A$/atom')
            axes[0][4].set_ylabel(r'$H$ (eV)')
            axes[0][4].set_title('Enthalpy per Volume')
            axes[1][3].set_ylabel(r'$E$ (eV)')
            axes[1][3].set_title('Energy per Volume')
            axes[1][4].set_ylabel(r'$P$ (kB)')
            axes[1][4].set_title('Pressure per Volume')
"""
    #plt.tight_layout()
    if display_graph:
        plt.show()
    elif not display_graph:
        plt.savefig("t3_energy_vs_volume.png")
    return


#print(column_text_read('t3_data'))
#print(energy_change(column_text_read('t3_data')))
print(plot_data(column_text_read('t3_data'), True),
      enthalpy_check(column_text_read('t3_data'))
      )
