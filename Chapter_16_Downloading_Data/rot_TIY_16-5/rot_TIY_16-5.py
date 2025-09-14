""" Hong Rot : Explore : Fort Wayne """

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

city_data = pd.read_csv("fort_wayne_int_airport_3241705.csv")

dates, snow_fall = [], []

for data in city_data["DATE"]:
    cur_date = datetime.strptime(data, "%Y-%m-%d")
    dates.append(cur_date)

for data in city_data["SNOW"]:
    try:
        snow_fall.append(float(data))
    except ValueError:
        snow_fall.append(None)


# plot the data

fig, ax = plt.subplots()
ax.plot(dates, snow_fall, color="blue")

ax.set_title("Daily Snow Fall 2013-2023", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()

ax.set_ylabel("Snow Fall (inches)", fontsize=16)

plt.show()
