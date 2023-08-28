import matplotlib.pyplot as plt

from plotting import data_read, plot_all_data
import numpy as np

labels = ["Pair Distance ($AA$^3)", "RDF (K)"]
pair_dist, rdf = data_read("T5_gC_rdf")
total_array = [pair_dist, rdf]

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
plt.axvline(x=new_pair_dist[min_index], ymin=0, ymax=0.12, color='k', label='minimum')
plt.annotate(f'first minimum = {new_rdf[min_index]}', xy=(new_pair_dist[min_index]+0.2, new_rdf[min_index]-0.2))
plot_all_data(total_array, 0, "pair distance ($\mathrm{\AA}^3$)", "RDF (g/$\mathrm{\AA}^3$)", "Radial Distribution Function", labels)
plt.grid()
plt.show()
#plt.savefig("RDF_gC")
