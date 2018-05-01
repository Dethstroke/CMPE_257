import pandas as pd
from sklearn import cluster
import kmeans

data = pd.read_csv('iris.data.txt', header = None)


training_data = data[0:112]

other_data = data[113:]

print (other_data)

