import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot
import plotly.express as px

from plotly.offline import  download_plotlyjs, init_notebook_mode, plot, iplot
# init_notebook_mode(connected=True)

import plotly.express as px


def run():
    # Historical stocks price dataset
    datafile = pd.read_csv('Dataset/dataset2.csv')

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
    figplot = go.Figure(data = company_data, layout=layout)
    figplot.write_html("templates/historicalplot.html")

    #iplot(plot)  # plotting graph


    #Objective 1: Using Linear Regression

    from sklearn.model_selection import train_test_split

    #Preprocessing
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.preprocessing import StandardScaler

    #Model Evaluation
    from sklearn.metrics import  mean_squared_error as mse
    from sklearn.metrics import r2_score

    #Traning and Testing  Data Split

    X = np.array(datafile.index).reshape(-1,1)
    Y = datafile['Close']
    X_train , X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.3, random_state=101)

    #features scaling
    scaler = StandardScaler().fit(X_train)

    from  sklearn.linear_model import  LinearRegression

    #creating a liner model
    lm = LinearRegression()
    lm.fit(X_train,Y_train)

    #plotting actual and predicted values

    trace0 = go.Scatter(
        x = X_train.T[0],
        y = Y_train,
        mode = 'markers',
        name = 'Actual'

    )

    trace1 = go.Scatter(
        x = X_train.T[0],
        y = lm.predict(X_train).T,
        mode='lines',
        name = 'Predicted'

    )

    company_data = [trace0,trace1]
    layout.xaxis.title.text = 'Day'
    figplot2 = go.Figure(data=company_data, layout=layout)
    figplot2.write_html("templates/historicalpredicted.html")



    # datafile = datafile[['Adj Close']]
    #
    # print(datafile)
    #
    # #printing info
    # print(datafile.info())

    #calculate scores for evaluation of model
    scores = f'''
    {'Metric'.ljust(10)}{'Train'.center(20)}{'Test'.center(20)}
    {'r2_score'.ljust(10)}{r2_score(Y_train, lm.predict(X_train))}\t{r2_score(Y_test, lm.predict(X_test))}
    {'MSE'.ljust(10)}{mse(Y_train, lm.predict(X_train))}\t{mse(Y_test, lm.predict(X_test))}
    '''

    print(scores)

if __name__ == '__main__':
    run()