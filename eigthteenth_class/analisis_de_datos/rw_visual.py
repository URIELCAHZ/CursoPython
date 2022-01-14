
import matplotlib.pyplot as plt

from walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use("classic")

fig, ax = plt.subplots()


point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, s = 10, c =point_numbers, cmap= plt.cm.Blues, edgecolors= "none")

ax.scatter(0, 0, c="green", edgecolors="none", s=50)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", s=50)




plt.show()