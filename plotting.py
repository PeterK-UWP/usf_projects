import matplotlib.pyplot as plt
import numpy as np

#print(plt.style.available)
#plt.style.use('classic')
# '_classic_test_patch', 'bmh', 'classic', 'fast', 'ggplot',
# 'grayscale', 'seaborn-v0_8-talk', 'seaborn-v0_8-paper', bold axis, bold title,


def data_read(filename):
    try:
        file = open(filename)
    except OSError as error:
        print(error)
        return

    content = file.readlines()
    number_of_data_sets = len(content[0].split())
    data = np.zeros([number_of_data_sets, (len(content))], float)
    n = 0

    for line in content:
        elements = line.split()
        for i in range(0, number_of_data_sets):
            data[i, n] = float(elements[i])
        n += 1
    return data


def plot_all_data(full_data_array, x_index, x_label, y_label, title, labels):
    # test if the x_index is in the full_data_array
    try:
        full_data_array[x_index]
    except IndexError:
        print("x_index doesn't exist!")

    x_values = full_data_array[x_index]  # need a universal x axis
    # redefine the y values
    for i in range(0, len(full_data_array)):
        if i != x_index:
            y_values = full_data_array[i]
            plt.plot(x_values, y_values, label=labels[i])  # this excludes the x_label
            plt.scatter(x_values, y_values)
            plt.xlabel(x_label, fontsize=18)
            plt.ylabel(y_label, fontsize=18)
            plt.title(title, fontsize=20)

            # print(y_values)
        else:
            continue

    plt.legend()
    # plt.show()
    # plt.savefig(title)
    return print('combined graph produced')


def plot_separate_data(full_data_array, x_index_value, y_index_value, x_label, y_label, title): #, windows):
    # Running average inclusion
    """
    average_y_values = []
    for j in range(len(full_data_array[y_index_value]) - windows + 1):
        average_y_values.append(np.mean(full_data_array[y_index_value][j:j + windows]))
    for j in range(windows - 1):
        average_y_values.insert(0, np.nan)

    plt.plot(full_data_array[x_index_value], average_y_values, 'k.-', label='running average')
    # color='k', linestyle='-', marker='.', linewidth=3
    """
    plt.plot(full_data_array[x_index_value], full_data_array[y_index_value], 'b.-', label=y_label)
    # color='b', linestyle='-', marker='.',



    # plt.scatter(full_data_array[x_index_value], full_data_array[y_index_value])
    plt.xlabel(x_label, fontsize=18)
    plt.ylabel(y_label, fontsize=18)
    plt.title(title, fontsize=20)

    plt.legend()
    plt.grid()
    plt.tight_layout()
    # plt.show()
    # plt.savefig(title)
    return print('specific plot created')


if __name__ == "__main__":
    """
    # this first statement confirms your data set as an input
    print(data_read("y=x^2"))
    
    # this second call plots all data against one set of data according to the x_index value.
    # use the label array for the legend outputs
    label_array = ['x', 'y^2', 'y^3']
    print(plot_all_data(data_read("y=x^2"), 0, "x-axis", "y-axis", "y=x^2&y=x^3", label_array))

    # this last call can plot any two data sets together given their index values
    print(plot_separate_data(data_read("y=x^2"), 0, 1, "y^3", "x", "y^3 vs x"))
    """
    print(data_read("y=x^2"))

    # label_array = ['nodes', 'time/node', 't1/tN']
    # print(plot_all_data(data_read("data.txt"), 0, "no. nodes", "time", "Effectiveness", label_array))

    # print(plot_separate_data(data_read("data.txt"), 0, 1, "nodes", "t1", "time per node"))
    print(plot_separate_data(data_read("y=x^2"), 0, 1, 'x', 'y', 'y=x^2', 5))
    # print(running_average(data_read("y=x^2"), 5))
    # label_array = ['x', 'y^2', 'y^3', 'run_avg']

    # print(plot_all_data(running_average(data_read("y=x^2"), 5), 0, "x", "y", "y=x^2", label_array))
