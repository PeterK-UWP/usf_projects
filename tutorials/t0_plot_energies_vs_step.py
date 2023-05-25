import numpy as np
import matplotlib.pyplot as plt


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


def plot_data(data):
    x_data = data[0]
    plt.xlabel('ionic step')
    y_data = data[1]
    plt.ylabel(r'$E$ (eV/atom)')
    plt.plot(x_data, y_data)

    plt.show()
    return

print(two_column_text_read('t0_data'))
print(plot_data(two_column_text_read('t0_data')))
