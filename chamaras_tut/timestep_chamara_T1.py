import numpy as np
import matplotlib.pyplot as plt
from plotting import data_read, plot_separate_data

# data file names here
data_files = ["0.5fs.dat", "1.0fs.dat", "2.0fs.dat", "3.0fs.dat", "4.0fs.dat"]
# input data to be processed
for file in data_files:
    contents = data_read(file)
    plot_separate_data(contents, 0, 1, "$t$ (ps)", "$E$ (eV/atom)", file, 10)
    # running average is plotted too
    # strip .dat and change . to _
    name = file.replace('.', '_')
    name = name.replace('_dat', '')
    plt.savefig(name)
    plt.show()
for file in data_files:
    contents = data_read(file)
    # cannot use plot all data, as the x values have separate lengths
    plt.plot(contents[0], contents[1], label=file)
plt.title("Energy vs Time-step", fontsize=20)
plt.xlabel("$t$ (ps)", fontsize=18)
plt.ylabel("$E$ (eV/atom)", fontsize=18)
plt.legend()
plt.tight_layout()
plt.savefig("compared_timesteps")
plt.show()


