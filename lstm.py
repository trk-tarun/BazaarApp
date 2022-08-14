import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense,LSTM,Dropout

#training dataset

data = pd.read_csv('Dataset2/apple_train_dataset.csv')
data.info
data["Close"] = pd.to_numeric(data.Close,errors='coerce')
data=data.dropna()
trainData = data.iloc[:, 4:5].values

data.info()

sc =