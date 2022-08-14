import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



import chart_studio.plotly as py
from plotly import graph_objs as go
from plotly.offline import plot




# Historical stocks price dataset
datafile = pd.read_csv('Dataset\dataset2.csv')

#print(datafile) #test datafile

datafile.info()

#reindexing using DateTimeIndex
datafile['Date'] = pd.to_datetime(datafile['Date'])

print(f'Dataframe between{datafile.Date.min()}{datafile.Date.max()}')
print(f'Total Days = {(datafile.Date.max() - datafile.Date.min()).days} days')
#summary of dataset

#print(datafile.describe())

datafile[['Open', 'High', 'Low', 'Close', 'Adj Close']].plot(kind='box')

#Objective 1: Using Linear Regression



# datafile = datafile[['Adj Close']]
#
# print(datafile)
#
# #printing info
# print(datafile.info())


