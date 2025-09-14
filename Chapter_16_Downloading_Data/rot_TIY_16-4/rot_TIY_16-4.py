""" Hong Rot : Automatic Indexing """

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# select city
print("Pick a city to measure temperature:")
while True:
    city_choice = input("1. Sitka, Alaska\n2. Death Valley, California\n3. San Francisco, California\n")
    if city_choice == "1":
        city = "sitka_airport_3237771.csv"
        break
    elif city_choice == "2":
        city = "death_valley_national_park_3237770.csv"
        break
    elif city_choice == "3":
        city = "san_francisco_int_airport_temperature_3237648.csv"
        break

# get temperature from this file

city_data = pd.read_csv(city)

dates, temperatures = [], []

for data in city_data["DATE"]:
    if data.startswith("2021"):  # only get 2021 data
        cur_date = datetime.strptime(data, "%Y-%m-%d")
        dates.append(cur_date)
    else:
        dates.append(None)

for data in city_data["TMAX"]:
    try:
        temperatures.append(int(data))
    except ValueError:
        temperatures.append(None)

# plot the temperatures

fig, ax = plt.subplots()
ax.plot(dates, temperatures, color="red")

ax.set_title("Daily High Temps 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()

plt.show()
