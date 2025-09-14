"""Hong Rot : Cubes - Colormap"""

import matplotlib.pyplot as plt

# plot 1 - first 5 cubes

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
plt.show()

# plot 2 - first 5000 cubes

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
plt.show()
