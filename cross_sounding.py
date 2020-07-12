import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = 'MALUKU_PERUM.csv'

data = pd.read_csv(file, sep=',', header=0)
data["datetime"] = data["date"] +" "+ data["time"]
data = data.drop(["date", "time"], axis=1)
print(data)
print(data)

###DATA
###CEK
