#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as np
import numpy as np
import matplotlib.pyplot as plot
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_acf 
register_matplotlib_converters

st.title("📈 Stock Price Viewer")

# Search bar
tickerSymbol = st.text_input("Enter a stock ticker (e.g., AAPL, MSFT):", "AAPL")


# In[4]:


import yfinance as yf


# In[9]:


# defines the ticker symbol of the stock

tickerSymbol = 'SPY'

# gets data on this ticker

tickerData = yf.Ticker(tickerSymbol)


# gets historical prices for the ticker
ticker_Df = tickerData.history(start='2015-1-1', end='2020-1-1')

print(ticker_Df.tail())


# In[ ]:


# Plots the data

plot.figure(figsize=(10,4))
plot.plot(ticker_Df.Close)
plot.title('Stock Price Over Time (%s)'%tickerSymbol, fontsize=20)
plot.ylabel('Price', fontsize=16)


