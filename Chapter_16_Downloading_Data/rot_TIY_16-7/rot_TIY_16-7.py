""" Hong Rot : Automated Title """

import json

import plotly.express as px

# Read data as a string and convert to a Python object. in UTF-8 because unknown character :(
file = 'eq_data/eq_data_30_day_m1.geojson'
with open(file, encoding='utf-8') as f:
    all_eq_data = json.load(f)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, long, lats, eq_titles = [], [], [], []
title = all_eq_data['metadata']['title']
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    long.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

fig = px.scatter_geo(lat=lats, lon=long, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()
