import numpy as np
import matplotlib.pyplot as plt
from plotting import data_read, plot_separate_data

data_files = ["0.5fs.dat", "1.0fs.dat", "2.0fs.dat", "3.0fs.dat", "4.0fs.dat"]

for file in data_files:
    contents = data_read(file)
    plot_separate_data(contents, 0, 1, "$t$ (ps)", "$E$ (eV/atom)", file, 10)
    # plot running average too

    plt.show()
for file in data_files:
    contents = data_read(file)
    # cannot use plot all data, as the x values have separate lengths
    plt.plot(contents[0], contents[1], label=file)
plt.title("Energy vs Time-step")
plt.xlabel("$t$ (ps)")
plt.ylabel("$E$ (eV/atom)")
plt.legend()
plt.show()
plt.savefig("compared_timesteps")


