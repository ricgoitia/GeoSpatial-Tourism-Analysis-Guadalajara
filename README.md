# Geospatial Tourism Analysis in Guadalajara

## Description

This project demonstrates a geospatial analysis of tourist attractions in Guadalajara, Jalisco, Mexico using Python.

The project uses:

- Pandas
- NumPy
- Folium
- MarkerCluster
- HeatMap

to create an interactive map that visualizes:

- Tourist attraction locations
- Estimated visitors
- Visitor satisfaction ratings
- Heat map of tourist concentration

## Dataset

The dataset contains simulated tourism data for locations in Guadalajara.

Each record includes:

- Name
- Latitude
- Longitude
- Number of visitors
- Satisfaction rating
- Type of attraction

## Technologies

```python
import folium
import pandas as pd
import numpy as np
from folium.plugins import MarkerCluster, HeatMap
