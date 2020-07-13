import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial import distance

file = 'MALUKU_PERUM.csv'

#Import data
data = pd.read_csv(file, sep=',', header=0)
data["datetime"] = data["date"] +" "+ data["time"]
data = data.drop(["date", "time"], axis=1)
data["datetime"] = pd.to_datetime(data["datetime"], dayfirst=True)

#Find Closest Point
data_all = data[['x','y','z','datetime']].to_numpy()

data_len = len(data_all)


# def closest_node(table1, table2):
#     closest_index = distance.cdist([table1], table2).argmin()
#     return table2[closest_index]

# closest_node(data_xy, data_xy)
# #print(data_xy[1])
