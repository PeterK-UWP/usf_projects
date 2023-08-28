# data has contains: chunk no. z (nm), P_zz (GPa), Temp (K)
# get z values from 20 - 30 in data1
#                   25-30 in data 3, 35-55in data 5 and 25-35 in data 7

import matplotlib.pyplot as plt
import numpy as np
from plotting import data_read, plot_separate_data

files = ["data_1kms", "data_3kms", "data_5kms", "data_7kms"]

# get index values (probably could simplify with a dictionary)
"""
data_dictionary = {'data_1kms': {},
                   'data_3kms': {},
                   'data_5kms': {},
                   'data_7kms': {}}
for file, data in data_dictionary:
"""
data = []
indexes_to_analyze = []
for file in files:
    if file == "data_1kms":
        all_data_1km = (data_read(file))
        data.append(all_data_1km)
        positions_1km = all_data_1km[1]
        data_of_interest_1km = []  # index values here
        for pos in positions_1km:
            if pos < 20 or pos > 30:
                continue
            elif 20 <= pos <= 30:
                data_of_interest_1km.append(list(positions_1km).index(pos))
        indexes_to_analyze.append(data_of_interest_1km)
        # print(data_of_interest_1km)

    elif file == "data_3kms":
        all_data_3km = (data_read(file))
        data.append(all_data_3km)
        positions_3km = all_data_3km[1]
        data_of_interest_3km = []
        for pos in positions_3km:
            if pos < 25 or pos > 30:
                continue
            elif 25 <= pos <= 30:
                data_of_interest_3km.append(list(positions_3km).index(pos))
        indexes_to_analyze.append(data_of_interest_3km)
        # print(data_of_interest_3km)

    elif file == "data_5kms":
        all_data_5km = (data_read(file))
        data.append(all_data_5km)
        positions_5km = all_data_5km[1]
        data_of_interest_5km = []
        for pos in positions_5km:
            if pos < 35 or pos > 55:
                continue
            elif 35 <= pos <= 55:
                data_of_interest_5km.append(list(positions_5km).index(pos))
        indexes_to_analyze.append(data_of_interest_5km)
        # print(data_of_interest_5km)

    elif file == "data_7kms":
        all_data_7km = (data_read(file))
        data.append(all_data_7km)
        positions_7km = all_data_7km[1]
        data_of_interest_7km = []
        for pos in positions_7km:
            if pos < 25 or pos > 35:
                continue
            elif 25 <= pos <= 35:
                data_of_interest_7km.append(list(positions_7km).index(pos))
        indexes_to_analyze.append(data_of_interest_7km)
        # print(data_of_interest_7km)

# print(indexes_to_analyze)

# data[file data][individual columns][index per column]
# data_to_analyze = []

data1 = data[0]
data3 = data[1]
data5 = data[2]
data7 = data[3]
pressures = [data1[2][indexes_to_analyze[0]],
             data3[2][indexes_to_analyze[1]],
             data5[2][indexes_to_analyze[2]],
             data7[2][indexes_to_analyze[3]]]
temperatures = [data1[3][indexes_to_analyze[0]],
                data3[3][indexes_to_analyze[1]],
                data5[3][indexes_to_analyze[2]],
                data7[3][indexes_to_analyze[3]]]

# print(pressures, temperatures)
average_pressures = []
average_temperatures = []
for press_dat in pressures:
    number_of_values_p = len(press_dat)
    average_pressures.append(sum(press_dat)/number_of_values_p)
for temps in temperatures:
    number_of_values_t = len(temps)
    average_temperatures.append(sum(temps)/number_of_values_t)
# print(average_pressures, average_temperatures)


##########___DATA_GRAPHS___#############
piston_velocities = [1, 3, 5, 7]
shock_velocities = [2.95, 6.33, 10.167, 13.33]
full_array = [piston_velocities, shock_velocities, average_pressures, average_temperatures]
print(f'piston_vel: {full_array[0]}')
print(f'shock_vel: {full_array[1]}')
print(f'average_press: {full_array[2]}')
print(f'average_temp: {full_array[3]}')

#plot_separate_data(full_array, 0, 1, "$v_p (km/s)$", "$v_s (km/s)$", "Shock Velocity vs Piston Velocity")
#plt.savefig('Shock vs Piston Velocity')

#x = np.arange(0, 8, 1)
#y = np.exp(0.9*x) + 12
#x = np.arange(0, 10, 1)
#y = 3.6*x**2 + 11
#plt.plot(x, y, color='y')
#plot_separate_data(full_array, 0, 2, "$v_p (km/s)$", "$P_{zz} (GPa)$", "Average Pressure vs Piston Velocity")
#plt.show()
#plt.savefig('Pressure vs Piston Velocity')

#plot_separate_data(full_array, 0, 3, "$v_p (km/s)$", "$T (K)$", "Average Temperature vs Piston Velocity")
#plt.savefig('Temperature vs Piston Velocity')
#plt.show()






"""
    indexes_to_analyze = [data_of_interest_1km, data_of_interest_3km, data_of_interest_5km, data_of_interest_7km]
    # print(data)
    data_to_analyze = []
    for data_set in indexes_to_analyze:
        for index in data_set:
            data_to_analyze.append(data[file][data_set][index])

print(data_to_analyze)

for index_data in indexes_to_analyze:
    for index in index_data:
        # data[all file data][individual columns][index per column]
        data_to_analyze.append(data[index_data][index])




"""
# data[0] from data1 ... data[3] from data7
