import numpy as np
"""
This code reads t3 data outputs the energy change between each ionic step, calculates enthalpy, and normalizes 
the energy and volume to be used for the EoS plot.
"""

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


def enthalpy(data):  # units dont match
    energy = np.array(data[1])
    pressure = (np.array(data[2]) + np.array(data[3]))*10**8  # Pa
    volume = np.array(data[4])*10**-30  # m^3
    theoretical_enthalpy_array = energy + (pressure * volume) * 6.242*10**18  # eV
    # calculated_enthalpy = data[8] / 2 error and inconsistent in VASP
    return theoretical_enthalpy_array / 2  # eV/atom


def energy_volume(data):
    energy = np.array(data[1]) # eV
    volume = np.array(data[4]) # A^3
    normalized_energy = energy / 2  # eV/atom
    normalized_volume = volume / 2  # A^3/atom
    normalized_data = normalized_volume, normalized_energy
    return normalized_data


#print(column_text_read('t3_data'))
#print(energy_change(column_text_read('t3_data')))
print(f'volume, energy:')
print(energy_volume(column_text_read('t3_data')))
print(f'does the pressure reduce to 5 GPa')
print(f'yes 50.00 kB converts to 5 GPa')
print('calculated enthalpy data is:')
print(enthalpy(column_text_read('t3_data')))

