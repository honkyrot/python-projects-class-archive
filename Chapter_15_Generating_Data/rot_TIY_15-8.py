""" Hong Rot : Multiplication """

import pandas as pd
from random import randint
import plotly.express as px


class Die:
    """Class to represent a single die"""

    def __init__(self, num_sides=6):
        self.times_rolled = 0
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides"""
        self.times_rolled += 1
        return randint(1, self.num_sides)


die_1 = Die(num_sides=6)
die_2 = Die(num_sides=6)
results = []

for noll_num in range(100000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualize the results
title = "rolling 2 dice X times"
labels = {"x": "result", "y": "frequency"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)

fig.show()
