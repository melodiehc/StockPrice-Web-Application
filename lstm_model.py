

# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import datetime
import yfinance as yf
import sklearn
from sklearn.preprocessing import StandardScaler
from google.colab import files

# Setting start and end dates for stock data
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 12, 31)

# Downloading stock data for 'AAPL' using yahoo finance
df = yf.download('AAPL', start=start, end=end)

# Data Preprocessing
df.head()
df.tail()
df = df.reset_index()
df.head()
df = df.drop(['Date', 'Adj Close'], axis = 1)
df.head()
plt.plot(df.Close)

# Calculating Moving Averages
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(100).mean()

# Data Splitting
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])

# Data Scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
scaler = StandardScaler()
data_training_array = scaler.fit_transform(data_training)

# Prepare Training Data for LSTM model
x_train = []
y_train = []
for i in range(100, data_training_array.shape[0]):
    x_train.append(data_training_array[i - 100: i])
    y_train.append(data_training_array[i, 0])

# Creating LSTM Model
from keras.layers import Dense, Dropout, LSTM
from keras.models import Sequential
model = Sequential()
#... LSTM model architecture ...

# Training the LSTM model
model.compile(optimizer = 'adam', loss = 'mean_squared_error')
model.fit(x_train, y_train, epochs = 50)

# Saving the model
model.save('keras_model.h5')

# Data Testing for LSTM model
data_testing.head()

# Data Preparation for Testing
final_df = past_100_days.append(data_testing, ignore_index = True)
input_data = scaler.fit_transform(final_df)
x_test = []
y_test = []
#... Prepare test data for LSTM model ...

# Making Predictions
y_predicted = model.predict(x_test)

# Data Scaling back to original scale
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor

# Visualizing Predictions vs Actual Prices
plt.figure(figsize=(12,6))
plt.plot(y_test, 'b', label = 'Original Price')
plt.plot(y_predicted, 'r',label = 'Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

# Save and Download the model
model.save('keras_model.h5')
files.download('keras_model.h5')
