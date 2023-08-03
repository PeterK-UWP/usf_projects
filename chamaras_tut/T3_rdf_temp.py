import matplotlib.pyplot as plt
from plotting import data_read, plot_all_data
import numpy as np

labels = ["Pair Distance ($AA$^3)", "RDF 5000K", "RDF 8000K"]
temperatures = ["rdf_5000.dat", "rdf_8000.dat"]
pair_dist_5K, rdf_5K = data_read(temperatures[0])
pair_dist_8K, rdf_8K = data_read(temperatures[1])


if len(pair_dist_5K) == len(pair_dist_8K):
    print('x_values match in length')
else:
    print('lengths do not match!')

pair_dist = pair_dist_5K
total_array = [pair_dist, rdf_5K, rdf_8K]

print(len(pair_dist), len(rdf_5K), len(rdf_8K))
#plot_all_data(full_data_array, x_index, x_label, y_label, title, labels):
plot_all_data(total_array, 0, "pair distance ($\mathrm{\AA}^3$)", "RDF (g/$\mathrm{\AA}^3$)", "Radial Distribution Function", labels)
#plt.show()
plt.savefig("RDF_diamond")
