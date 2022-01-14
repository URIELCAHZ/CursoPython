from matplotlib import pyplot

pyplot.style.use("seaborn")



fig, ax = pyplot.subplots()

x_values = list(range(1,6))
y_values = [x*x for x in x_values]

# ax.scatter(x_values, y_values, s=50, c =(0,0,0))
ax.scatter(x_values, y_values, s=50, c =x_values, cmap= pyplot.cm.Blues)


ax.set_title("Squares Numbers")
ax.set_xlabel("Value")
ax.set_ylabel("Squares values")

ax.tick_params(axis = "both")
ax.axis([0, 10, -1, 30])

pyplot.savefig("squares_plot.png", bbox_inches = "tight")

pyplot.show()