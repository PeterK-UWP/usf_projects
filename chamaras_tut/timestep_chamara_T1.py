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
        data[0, n] = float(elements[0])  # time
        data[1, n] = float(elements[1])  # etot

        n += 1

    return data


def plot_data(data_array, data_list):  # T1: include data_list for T1, data_list): #, display_graph):
    for x, y in data_array:
        plt.xlabel('time (ps)')
        plt.ylabel(r'$E$ (eV/atom)')
        plt.xlim(0, 60)
        plt.plot(x, y)
        #plt.scatter(x, y)
    plt.title('Total_Energy vs Timesteps')
    plt.tight_layout()
    plt.show()
    plt.legend([1.0, 0.5, 2.0, 3.0, 4.0])
    return


    plt.xlabel('time (ps)')
    plt.ylabel(r'$E$ (eV/atom)')
    plt.xlim(0, 60)
    plt.plot(data_array[0], data_array[1], color='orange')
    plt.scatter(data_array[0], data_array[1], color='orange')
    plt.tight_layout()
    plt.title('Total_Energy vs Timesteps')
    if display_graph:
        plt.show()
    elif not display_graph:
        plt.savefig("orange_etotal_vs_time_.0.5.png")

    return


if __name__ == "__main__":

    ##############################
    #Tutorial 1
    # print(plot_data(two_column_text_read('0.5fs.dat'), False))

    data = ['0.5fs.dat', '1.0fs.dat', '2.0fs.dat', '3.0fs.dat', '4.0fs.dat']
    data_array = []
    for i in data:
        data_array.append((two_column_text_read(i)))
    plot_data(data_array, data)
    plt.show()
    #print(plot_data(two_column_text_read(data), True))  # True for graph, False to save png


