from plotting import plot_separate_data, data_read, plot_all_data
import matplotlib.pyplot as plt
import numpy as np

def minimum_rdf(filename): #, labels, titles):
    pair_dist, rdf = data_read(filename)
    total_array = [pair_dist, rdf]
    labels = ["1km", "3km", "5km", "7km"]
    #labels = ["Pair Distance ($AA$^3)", "RDF (K)"]

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
    #plt.axvline(x=new_pair_dist[min_index], ymin=0, ymax=0.16, color='k', label='minimum')
    #plt.annotate(f'first minimum = {new_pair_dist[min_index]},{new_rdf[min_index]}',
     #            xy=(new_pair_dist[min_index] + 0.2, new_rdf[min_index] - 0.2))
    #plot_all_data(total_array, 0, "pair distance ($\mathrm{\AA}$)", "RDF",
     #             "Radial Distribution Function", labels)
    plt.plot(pair_dist, rdf, label=filename)
    plt.xlabel("pair distance ($\mathrm{\AA}$)", fontsize=18)
    plt.ylabel("RDF", fontsize=18)
    plt.title("Radial Distribution Function", fontsize=20)
    plt.legend()
    plt.grid()
    #plt.show()
    #plt.savefig(filename)

    return new_pair_dist, new_rdf


def coordination(filename):
    no_of_bonds, ratio = data_read(filename)
    for i in np.linspace(0, len(ratio) - 1, len(ratio)):
        i_int = int(i)
        plt.annotate(f' {ratio[i_int]:0.2f}% ', xy=(no_of_bonds[i_int] - 0.5, ratio[i_int] + 0.7))

    plt.scatter(no_of_bonds, ratio, label=filename)
    plt.plot(no_of_bonds, ratio)
    #print(no_of_bonds, ratio)
    plt.xlabel("no. of bonds", fontsize=18)
    plt.ylabel("bond ratio", fontsize=18)
    plt.title("Ratio of Bonds", fontsize=20)
    plt.legend()
    #plt.show()
    #plt.savefig(filename)
    return no_of_bonds, ratio


if __name__=='__main__':
    coord_files = ["coord_1km", "coord_3km", "coord_5km", "coord_7km"]
    rdf_files = ["rdf_1km", "rdf_3km", "rdf_5km", "rdf_7km"]
    #for file in rdf_files:
    #    minimum_rdf(file)
    for file in coord_files:
        coordination(file)
    #plt.show()
    plt.savefig("combined_coordination_plot_annotated")

    #coordination(coord_files[3])
"""
    rdf_files = ["rdf_1km", "rdf_3km", "rdf_5km", "rdf_7km"]
    coord_files = ["coord_1km", "coord_3km", "coord_5km", "coord_7km"]
    color_list = ['b', 'o', 'g', 'r']
    labels = []
    titles = []
    rdf_coord_plot(rdf_files, coord_files)
#print(full_rdf_array[1])  # 0 is the x array, 1 is the WHOLE y array"""


