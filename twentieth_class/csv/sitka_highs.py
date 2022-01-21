import csv
import matplotlib.pyplot as plt
from datetime import datetime



filename = "twentieth_class\csv\data\sitka_weather_2018_simple.csv"

with open(filename) as file:
    reader = csv.reader(file)
    header = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[-2])
        highs.append(high)
        low = int(row[-1])
        lows.append(low)
    
    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.plot(dates, highs, c = "red")
    ax.plot(dates, lows, c = "blue", alpha = 0.5)
    ax.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.3)
    

    ax.set_title( "Daily high and low temperatures, July 2018", fontsize = 24)
    ax.set_xlabel("")
    ax.set_ylabel("Temperature (F)", fontsize = 5)

    fig.autofmt_xdate()

    plt.show()



