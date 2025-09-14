"""Hong Rot : Modified Random Walk"""
import matplotlib.pyplot as plt

from random import choice


class RandomWalk:
    """Class to generate random walks"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, 0, -1])
            x_distance = choice(list(range(-11, 11)))**10
            x_step = x_direction * x_distance

            y_direction = choice([1, 0, -1])
            y_distance = choice(list(range(-11, 11)))**10
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


while True:
    rw = RandomWalk(10000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=2, c='rainbow')
    ax.set_aspect('equal')

    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_facecolor('black')

    plt.show()
    break
