import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


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
    volume = data[0]
    pressure = data[1]
    plt.plot(volume, pressure)
    plt.scatter(volume, pressure)
    plt.xlabel("volume")
    plt.ylabel("pressure")
    plt.title("press vs vol")
    plt.legend('Press')
    plt.show()
    return


def bivariate_statistics(data):
    if len(data) != 2 or len(data[0]) <= 1:
        raise IndexError

    stat = stats.stats.describe(data, axis=1)
    mean_of_y = stat.minmax[0][1]
    x_min, x_max = stat.minmax[0][0], stat.minmax[1][0]
    y_min, y_max = stat.minmax[0][1], stat.minmax[1][1]
    standard_deviation_of_y = np.sqrt(stat.variance[1])
    statistics = np.array([mean_of_y, standard_deviation_of_y, x_min, x_max, y_min, y_max])

    return statistics


if __name__ == '__main__':
    print(bivariate_statistics(two_column_text_read('vol_press_data')))
    print(plot_data(two_column_text_read('vol_press_data')))
