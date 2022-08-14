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

sc = MinMaxScaler(feature_range=(0,1))
trainData = sc.fit_transform(trainData)\
trainData.shape

###

X_train = []
Y_train = []

#60 is time step  ## 1149 = length of data

for i in range (60, 1149):
    X_train.append(trainData[i-60:i, 0])
    Y_train.append(trainData[i,0])

X_train,Y_train = np.array(X_train), np.array(Y_train)

X_train = np.reshape(X_train,(X_train.shape[0], X_train.shape[1],1))
X_train.shape
model = Sequential()

model.add(LSTM(units=100, return_sequences=True, input_shape=(X_train.shape[1],1)))
model.add(Dropout(0.2))

model.add(LSTM(units=100, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=100, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=100, return_sequences=True))
model.add(Dropout(0.2))

model.add(Dense(units=1))
model.compile(optimizer='adam', loss="mean_squared_error")
