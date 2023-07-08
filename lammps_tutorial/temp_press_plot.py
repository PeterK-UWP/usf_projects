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
    data = np.zeros([3, (len(content))], float)
    n = 0

    for line in content:
        elements = line.split()
        data[0, n] = float(elements[0])
        data[1, n] = float(elements[1])
        data[2, n] = float(elements[2])

        n += 1

    return data


def plot_data(data):
    timestep = data[0]
    temp = data[1]
    press = data[2]
    plt.plot(timestep, temp)
    plt.plot(timestep, press)
    plt.scatter(timestep, temp)
    plt.scatter(timestep, press)
    plt.xlabel("timestep")
    plt.ylabel("data")
    plt.title("temp & pressure vs timestep")
    plt.legend(['Temp', 'Press'])
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
    #print(bivariate_statistics(two_column_text_read('step_temp_press')))
    print(plot_data(two_column_text_read('step_temp_press')))
