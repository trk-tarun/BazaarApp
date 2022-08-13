import pandas as pd
import matplotlib.pyplot as plt




# Historical stocks price dataset
datafile = pd.read_csv('Dataset\dataset2.csv')

print(datafile) #test datafile

#summary of dataset

print(datafile.describe())

#Objective 1: Using Linear Regression

#reindexing using DateTimeIndex
datafile.set_index(pd.DatetimeIndex(datafile['Date']),inplace=True)

datafile = datafile[['Adj Close']]

print(datafile)

#printing info
print(datafile.info())


