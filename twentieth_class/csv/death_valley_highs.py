import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "twentieth_class\csv\data\death_valley_2018_full.csv"

with open(filename) as file:
    reader = csv.reader(file)
    next(reader)
    
    dates, temp_highs, temp_lows = [], [], []

    for row in reader:
        dates.append( datetime.strptime(row[2], "%Y-%m-%d"))
        temp_highs.append(int(row[-3]))
        temp_lows.append(int(row[-2]))

    plt.style.use("seaborn")

    
    fig, ax = plt.subplots()

    ax.plot(dates, temp_highs, c = "green")
    ax.plot(dates, temp_lows, c = "red")
    ax.fill_between(dates, temp_highs, temp_lows, facecolor = "blue", alpha = 0.5)

    ax.set_title("Death Valley 2018 temperatures", fontsize = 30  )
    ax.set_xlabel("Dates")
    ax.set_ylabel("Temperature in F°", fontsize = 10)
    fig.autofmt_xdate()

    plt.show()



