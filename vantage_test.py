# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:37:21 2019

@author: Warren.Gibson
"""

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import pandas as pd
import time

TodaysDate = time.strftime("%d-%m-%Y")
excelfilename = TodaysDate +".xlsx"

key = '04ZSXW5RLYE97YGI'
# Chose your output format, or default to JSON (python dict)
ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)

# Get the data, returns a tuple
# aapl_data is a pandas dataframe, aapl_meta_data is a dict
aapl_data, aapl_meta_data = ts.get_daily(symbol='AAPL')
# aapl_sma is a dict, aapl_meta_sma also a dict
aapl_sma, aapl_meta_sma = ti.get_sma(symbol='AAPL')

aapl_data.to_excel(excelfilename)



# Visualization
#figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
#aapl_data['4. close'].plot()
#plt.tight_layout()
#plt.grid()
#plt.show()