#Stock Price Web Application code 
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

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 12, 31)

st.title('Stock Trend Prediction')

user_input = st.text_input('Enter Stock Ticker', 'AAPL')
df = yf.download(user_input, start=start, end=end)

st.subheader('Data from 2010-2019')
st.write(df.describe())

#Visualizations 
st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize = (12,6))
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing Price vs Time Chart with 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing Price vs Time Chart with 100MA & 200MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()

fig = plt.figure(figsize = (12,6))
plt.plot(ma100)
plt.plot(ma200)
plt.plot(df.Close)
st.pyplot(fig)










