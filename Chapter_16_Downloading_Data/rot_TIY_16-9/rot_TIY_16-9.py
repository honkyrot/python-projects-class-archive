""" Hong Rot : Forest Fires """

import plotly.express as px
import pandas as pd

# csv file
file = 'data/world_fires_1_day.csv'
world_fires_file = pd.read_csv(file)

lat, lon, brightness, true_bright = [], [], [], []

for index, row in world_fires_file.iterrows():
    lat.append(row['latitude'])
    lon.append(row['longitude'])
    math_bright = (row['brightness'] // 100) ** 5
    brightness.append(math_bright)
    true_bright.append(row['brightness'])

fig = px.scatter_geo(lat=lat, lon=lon, size=brightness, title='World Fires',
                     color=true_bright,
                     color_continuous_scale='Hot',
                     labels={'color': 'Brightness'},
                     hover_name=true_bright,)
fig.show()
