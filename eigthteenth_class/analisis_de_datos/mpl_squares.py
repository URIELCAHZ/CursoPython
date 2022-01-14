from tkinter import font
import matplotlib.pyplot as plt

input_values = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4 , 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)

ax.set_title("Square numbers", fontsize = 14)
ax.set_xlabel("Value", fontsize = 16)
ax.set_ylabel("Square of value", fontsize = 16)

ax.tick_params(axis= "both", labelsize = 15)

plt.show()