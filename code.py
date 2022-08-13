import pandas as pd



# Historical stocks price dataset
datafile = pd.read_csv('Dataset\dataset2.csv')

#print(datafile) #test datafile

#summary of dataset

print(datafile.describe())

#Objective 1: Using Linear Regression

#reindexing using DateTimeIndex
datafile.set_index(pd.DatetimeIndex(datafile['Date']),inplace=True)