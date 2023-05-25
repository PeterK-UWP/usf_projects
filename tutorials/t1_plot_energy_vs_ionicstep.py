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


def energy_change(data):
    change_list = []
    for i in np.linspace(0, len(data[1])-1, 7):   # (0, ionic step - 1, ionic step)
        if i < 6:   # ionic step - 1
            change = data[1][int(i+1)] - data[1][int(i)]
            change_list.append(change)
        if i == 6:  # ionic step
            continue
    return change_list


def plot_data(data, display_graph):
    x_data = data[0]
    plt.xlabel('ionic step')
    y_data = data[1]
    plt.ylabel(r'$E$ (eV/atom)')
    plt.plot(x_data, y_data)
    plt.tight_layout()

    if display_graph:
        plt.show()
    elif not display_graph:
        plt.savefig("t1_energy_vs_ionic_step.png")
    return


print(two_column_text_read('t1_data'))
print(energy_change(two_column_text_read('t1_data')))
print(plot_data(two_column_text_read('t1_data'), True))  # True for graph, False to save png
