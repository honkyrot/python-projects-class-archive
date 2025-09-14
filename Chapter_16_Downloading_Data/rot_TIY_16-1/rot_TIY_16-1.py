""" Hong Rot : Stika Rainfall """

import csv
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

# get stika rainfall from this file

path = Path("sitka_airport_3237771.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, rainfall = [], []

for row in reader:
    cur_date = datetime.strptime(row[2], "%Y-%m-%d")
    rainfall.append(float(row[5]))
    dates.append(cur_date)

# get death valley rainfall from this file

path2 = Path("death_valley_national_park_3237770.csv")
lines2 = path2.read_text().splitlines()

reader2 = csv.reader(lines2)
header_row2 = next(reader2)

dates2, rainfall2 = [], []

for row in reader2:
    cur_date = datetime.strptime(row[2], "%Y-%m-%d")
    rainfall2.append(float(row[3]))
    dates2.append(cur_date)

# plotting

fig = plt.figure(figsize=(10, 6))

ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(dates, rainfall, color="green")
ax1.set_title("Rainfall in Sitka", fontsize=12)

ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(dates2, rainfall2, color="blue")
ax2.set_title("Rainfall in Death Valley", fontsize=12)

plt.show()
