# Stock Price Web Application code 

# Importing necessary libraries
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import datetime
import yfinance as yf
import streamlit as st
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from keras.layers import Dense, Dropout, LSTM
from keras.models import Sequential

# Define start and end dates for stock data
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 12, 31)

# Setting up Streamlit web application
st.title('Stock Trend Prediction')

# User input for stock ticker symbol
user_input = st.text_input('Enter Stock Ticker', 'AAPL')
df = yf.download(user_input, start=start, end=end)

# Display descriptive statistics of the stock data
st.subheader('Data from 2010-2019')
st.write(df.describe())

# Visualizations 

# Closing Price vs Time Chart
st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize = (12,6))
plt.plot(df.Close)
st.pyplot(fig)

# Closing Price vs Time Chart with 100-day Moving Average (MA)
st.subheader('Closing Price vs Time Chart with 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(fig)

# Closing Price vs Time Chart with 100-day and 200-day Moving Averages (MA)
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()

fig = plt.figure(figsize = (12,6))
plt.plot(ma100)
plt.plot(ma200)
plt.plot(df.Close)
st.pyplot(fig)
