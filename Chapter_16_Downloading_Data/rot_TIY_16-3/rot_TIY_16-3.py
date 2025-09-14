""" Hong Rot : San Francisco + """

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


# get stika temperature from this file

data1 = pd.read_csv("sitka_airport_3237771.csv")

dates, temperatures = [], []

for data in data1["DATE"]:
    cur_date = datetime.strptime(data, "%Y-%m-%d")
    dates.append(cur_date)

for data in data1["TMAX"]:
    try:
        temperatures.append(int(data))
    except ValueError:
        temperatures.append(None)

# get death valley temperature from this file

data2 = pd.read_csv("death_valley_national_park_3237770.csv")

dates2, temperatures2 = [], []

for data in data2["DATE"]:
    cur_date = datetime.strptime(data, "%Y-%m-%d")
    dates2.append(cur_date)

for data in data2["TMAX"]:
    try:
        temperatures2.append(int(data))
    except ValueError:
        temperatures2.append(None)

# get san francisco temperature from this file

data3 = pd.read_csv("san_francisco_int_airport_temperature_3237648.csv")

dates3, temperatures3 = [], []

for data in data3["DATE"]:  # trim date to 2021 because data is a 5-year range.
    if data.startswith("2021"):
        cur_date = datetime.strptime(data, "%Y-%m-%d")
        dates3.append(cur_date)
    else:
        dates3.append(None)

for data in data3["TMAX"]:
    try:
        temperatures3.append(int(data))
    except ValueError:
        temperatures3.append(None)

# plot the temperature comparison

fig, ax = plt.subplots()
ax.plot(dates, temperatures, color="red")
ax.plot(dates2, temperatures2, color="blue")
ax.plot(dates3, temperatures3, color="green")

ax.set_title("Daily High Temps 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()

ax.set_ylabel("Temperature (F)", fontsize=12)
ax.set_ylim([12, 132])
ax.set_yticks(range(0, 120, 4))
#ax.tick_params(labelsize=16)

# legend
ax.legend(["Sitka", "Death Valley", "San Francisco"])

plt.show()
