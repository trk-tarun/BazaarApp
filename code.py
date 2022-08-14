import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

from plotly.offline import  download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)



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

#layout for plot

layout = go.Layout(
    title = 'Stock Price of Company',
    xaxis = dict(
        title = 'Date',
        titlefont = dict(
            family = 'Ariel',
            size = 20,
            color='#000000'
        )

    ),

    yaxis = dict(
        title='Price',
        titlefont= dict(
            family ='Ariel',
            size=20,
            color='#000000'
        )
    )
)

company_data = [{'x':datafile['Date'], 'y':datafile['Close']}]
plot = go.Figure(data = company_data, layout=layout)

iplot(plot)  # plotting graph


#Objective 1: Using Linear Regression

from sklearn.model_selection import train_test_split

#Preprocessing




# datafile = datafile[['Adj Close']]
#
# print(datafile)
#
# #printing info
# print(datafile.info())


