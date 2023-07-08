import matplotlib.pyplot as plt
import numpy as np


def data_read(filename):
    try:
        file = open(filename)
    except OSError as error:
        print(error)
        return

    content = file.readlines()
    data = np.zeros([3, (len(content))], float)
    n = 0

    for line in content:
        elements = line.split()
        # nodes t1 t1/tN
        data[0, n] = float(elements[0])
        data[1, n] = float(elements[1])
        data[2, n] = float(elements[2])

        n += 1
    return data


print(data_read("data.txt"))
plt.plot(data_read("data.txt")[0], data_read("data.txt")[1])
plt.scatter(data_read("data.txt")[0], data_read("data.txt")[1])
plt.title("Time of Computation vs Nodes")
plt.xlabel("nodes")
plt.ylabel("Time (sec)")
plt.savefig("scaling_graph")
plt.show()
plt.plot(data_read("data.txt")[0], data_read("data.txt")[2])
plt.scatter(data_read("data.txt")[0], data_read("data.txt")[2])

x = np.linspace(0, 150, 10)
y = x
plt.plot(x, y)
plt.title("Effectiveness(t1/tN) vs Nodes")
plt.xlabel("nodes")
plt.ylabel("Time (sec)")
plt.legend(["y=x", "effectiveness_curve"])
plt.savefig("strong_scaling_graph")
plt.show()
