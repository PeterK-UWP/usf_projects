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

# use if you want all data in one file to plot against one column
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
            #plt.scatter(x_values, y_values)
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

# use if you have all data in one file to specify your y column
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


def minimum_rdf(full_data_array): #, labels, titles):
    pair_dist, rdf = full_data_array
    total_array = [pair_dist, rdf]
    labels = ["Pair Distance ($AA$^3)", "RDF (K)"]

    # find maximum and get its index
    max_index = max(enumerate(rdf), key=lambda x: x[1])[0]
    max_pair_dist = pair_dist[max_index]
    # print(max_pair_dist, max(rdf))

    # get the index values ranging from the max to the end
    index_values = np.linspace(max_index, len(pair_dist) - 1, len(pair_dist) - max_index)
    # print(index_values)

    # get minimum index of the rdf from the new bounds
    new_pair_dist = []
    new_rdf = []
    for i in index_values:
        int_i = int(i)
        new_pair_dist.append(pair_dist[int_i])
        new_rdf.append(rdf[int_i])
    # print(new_pair_dist, new_rdf)
    min_index = min(enumerate(new_rdf), key=lambda x: x[1])[0]
    print(new_pair_dist[min_index], new_rdf[min_index])
    # print(pair_dist[20], rdf[20])

    # plot vertical line where minimum is
    plt.axvline(x=new_pair_dist[min_index], ymin=0, ymax=0.2, color='k', label='minimum')
    plt.annotate(f'first minimum = {new_pair_dist[min_index]},{new_rdf[min_index]}',
                 xy=(new_pair_dist[min_index] + 0.2, new_rdf[min_index] - 0.2))
    plot_all_data(total_array, 0, "pair distance ($\mathrm{\AA}^3$)", "RDF (g/$\mathrm{\AA}^3$)",
                  "Radial Distribution Function", labels)
    plt.grid()
    #plt.show()
    #plt.savefig(filename)

    return new_pair_dist, new_rdf


def coordination(filename):
    no_of_bonds, ratio = data_read(filename)
    for i in np.linspace(0, len(ratio) - 1, len(ratio)):
        i_int = int(i)
        plt.annotate(f' {ratio[i_int]:0.2f} % ', xy=(no_of_bonds[i_int] - .5, ratio[i_int] + .5))
    plt.bar(no_of_bonds, ratio, color='blue')
    #print(no_of_bonds, ratio)
    plt.xlabel("no. of bonds", fontsize=18)
    plt.ylabel("bond ratio", fontsize=18)
    plt.title("Ratio of Bonds", fontsize=20)
    plt.show()
    #plt.savefig(filename)
    return no_of_bonds, ratio

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

    minimum_rdf("T5_gC_rdf")
    coordination("T5_gC_coord")
