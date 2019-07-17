import csv
import numpy as np
path = r'C:/projects/python/ml/data/iris.csv'

with open(path,'r') as f:
    reader = csv.reader(f,delimiter = ',')
    headers = next(reader)
    data = list(reader)
    #data = np.array(data).astype(float)
data = np.array(data)
#print(data.shape)
print(headers)
# print (data[:3])
