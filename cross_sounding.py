import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = 'MALUKU_PERUM.csv'

#Import data
data = pd.read_csv(file, sep=',', header=0)
data["datetime"] = data["date"] +" "+ data["time"]
data = data.drop(["date", "time"], axis=1)
data["datetime"] = pd.to_datetime(data["datetime"], dayfirst=True)

#Find Closest Point
data_x= data["x"]
data_x= data["y"]

