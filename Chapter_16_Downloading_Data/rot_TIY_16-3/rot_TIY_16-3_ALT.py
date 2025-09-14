""" Hong Rot : San Francisco w/ subplot2grid """

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

last_stored_data_fill = 0

# get stika temperature from this file

data1 = pd.read_csv("sitka_airport_3237771.csv")

dates1, t_high1, t_low1 = [], [], []

for data in data1["DATE"]:
    cur_date = datetime.strptime(data, "%Y-%m-%d")
    dates1.append(cur_date)

for data in data1["TMAX"]:
    try:
        t_high1.append(int(data))
        last_stored_data_fill = int(data)
    except ValueError:
        t_high1.append(last_stored_data_fill)

for data in data1["TMIN"]:
    try:
        t_low1.append(int(data))
        last_stored_data_fill = int(data)
    except ValueError:
        t_low1.append(last_stored_data_fill)

# get death valley temperature from this file

data2 = pd.read_csv("death_valley_national_park_3237770.csv")

dates2, t_high2, t_low2 = [], [], []

for data in data2["DATE"]:
    cur_date = datetime.strptime(data, "%Y-%m-%d")
    dates2.append(cur_date)

for data in data2["TMAX"]:
    try:
        t_high2.append(int(data))
        last_stored_data_fill = int(data)
    except ValueError:
        t_high2.append(last_stored_data_fill)

for data in data2["TMIN"]:
    try:
        t_low2.append(int(data))
        last_stored_data_fill = int(data)
    except ValueError:
        t_low2.append(last_stored_data_fill)

# get san francisco temperature from this file

data3 = pd.read_csv("san_francisco_int_airport_temperature_3237648.csv")

dates3, t_high3, t_low3 = [], [], []

for data in data3["DATE"]:  # trim date to 2021 because data is a 5-year range.
    if data.startswith("2021"):
        cur_date = datetime.strptime(data, "%Y-%m-%d")
        dates3.append(cur_date)
    else:
        dates3.append(None)

for data in data3["TMAX"]:
    try:
        t_high3.append(int(data))
        last_stored_data_fill = int(data)
    except ValueError:
        t_high3.append(last_stored_data_fill)

for data in data3["TMIN"]:
    try:
        t_low3.append(int(data))
        last_stored_data_fill = int(data)
    except ValueError:
        t_low3.append(last_stored_data_fill)

# plot the temperature comparison

fig = plt.figure()

# (X, Y) relative GRID SIZE (Y, X) GRID POSITION or square x in grid x
# colspan = X size
# rowspan = Y size

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax1.plot(dates1, t_high1, color="red")
ax1.plot(dates1, t_low1, color="blue")
ax1.fill_between(dates1, t_high1, t_low1, facecolor="purple", alpha=0.1)
ax1.set_title("Stika High Low Temperature", fontsize=11)

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=3)
ax2.plot(dates2, t_high2, color="red")
ax2.plot(dates2, t_low2, color="blue")
ax2.fill_between(dates2, t_high2, t_low2, facecolor="purple", alpha=0.1)
ax2.set_title("Death Valley High Low Temperature", fontsize=11)

ax3 = plt.subplot2grid((3, 3), (2, 0), colspan=3)
ax3.plot(dates3, t_high3, color="red")
ax3.plot(dates3, t_low3, color="blue")
ax3.fill_between(dates3, t_high3, t_low3, facecolor="purple", alpha=0.1)
ax3.set_title("San Francisco High Low Temperature", fontsize=11)

plt.show()
