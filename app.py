import pandas as pd
from fileinput import filename
import symbol
import talib
import os,csv
#from patterns import candlestick_patterns
import yfinance as yf

import pandas as pd
import numpy as np
import time
import datetime
import matplotlib.pyplot as plt
from sklearn import preprocessing
import os,csv
import matplotlib.dates as mdates
import matplotlib.dates as matdates

import seaborn as sns
import scipy.stats as stats
import pylab
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
from fileinput import filename
import talib
import os,csv
import glob
from flask import Flask, render_template, request, flash, redirect, jsonify
import yfinance as yf
######################KUCOIN############################
import numpy as np
from kucoin.client import Client
from kucoin.asyncio import KucoinSocketManager
import ccxt
from datetime import datetime
import time

import ccxt
import config
import schedule
import io
import io
import random
from flask import Response, send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import plotly.graph_objects as go

from flask_cors import CORS
import numpy as np
from kucoin.client import Client
from kucoin.asyncio import KucoinSocketManager
import ccxt
from datetime import datetime
import time


app = Flask(__name__)
CORS(app)
@app.route("/")

def index():

    return render_template('index1.html')

# @app.route('/history')
 
# def history():
#     now = datetime.now()
#     now = int(time.mktime(now.timetuple()))
#     period=['1min']
#     with open('datasets/symbol.csv') as f:
#         coins=f.read().splitlines()
#         for coin in coins:
#             coin=coin.split(',')[0]
#             pair=coin
#             for j in range(len(period)):

#                 candlesticks =  client.get_kline_data(pair,period[j],np.abs(int(now-50*60)),now)
#                 processed_candlesticks = []
#                 for data in candlesticks:
#                     candlestick = { 
#                         "time": data[0], 
#                         "open": data[1],
#                         "close": data[2], 
#                         "high": data[3], 
#                         "low": data[4],
#                         "Transamount": data[5],
#                         "Volume": data[6]
#                     }
#                     exclude_keys = ["Transamount", "Volume"]

#                     new_d = {k: candlestick[k] for k in set(list(candlestick.keys())) - set(exclude_keys)}
#                     new_d['time'] = int(new_d['time'])

#                     processed_candlesticks.append(new_d)

#                 processed_candlesticks=pd.DataFrame(processed_candlesticks)
#                 processed_candlesticks=processed_candlesticks[::-1]
#                 import json

#                 processed_candlesticks = json.loads(json.dumps(list(processed_candlesticks.T.to_dict().values())))

#     return jsonify(processed_candlesticks)