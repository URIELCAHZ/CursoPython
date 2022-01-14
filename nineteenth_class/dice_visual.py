from dice import Dice
from plotly.graph_objs import Bar, Layout
from plotly import offline

dice = Dice()

results = [dice.roll() for x in range(100)]

frecuencies = []

for value in range(1, dice.num_sides +1 ):
    frecuencies.append( results.count(value))

print(frecuencies)

x_values = list(range(1, dice.num_sides +1 ))
data = [Bar(x = x_values, y = frecuencies)]

x_axis_config = {"title": "Results"}
y_axis_config = {"title": "Results frecuency"}

layout = Layout(title = "Results of rolling one die 100 times", xaxis= x_axis_config, yaxis = y_axis_config)

offline.plot({"data": data, "layout": layout}, filename = "dieFrequencies.html")
