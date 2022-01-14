
import matplotlib.pyplot as plt

from walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use("classic")

fig, ax = plt.subplots()

ax.scatter(rw.x_values, rw.y_values, s = 10, c =rw.z_values, cmap= plt.cm.Blues)

plt.show()