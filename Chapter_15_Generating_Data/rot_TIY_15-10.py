"""Hong Rot : Practicing with Both Libraries"""
import matplotlib.pyplot as plt
from random import randint
from random import choice
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


class RandomWalk:
    """Class to generate random walks"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    @staticmethod
    def get_step():
        direction = choice([1, 0, -1])
        distance = choice(list(range(-11, 11))) ** 10
        step = direction * distance
        return step

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


die_1 = Die()
die_results = []

for noll_num in range(10000):
    result = die_1.roll()
    die_results.append(result)

die_max_result = die_1.num_sides
die_poss_results = range(3, die_max_result + 1)
die_frequency = [die_results.count(value) for value in die_poss_results]

print(die_frequency)
plt.plot(die_frequency, linewidth=5, color="red")

plt.show()

rw = RandomWalk()
rw.fill_walk()

fig = px.line(x=rw.x_values, y=rw.y_values, title="Random Walk", labels={"x": "x", "y": "y"})

fig.show()
