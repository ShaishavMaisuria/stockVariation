#https://www.datacamp.com/community/tutorials/finance-python-trading?utm_source=adwords_ppc&utm_campaignid=1565261270&utm_adgroupid=67750485268&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=1t4&utm_creative=332661264365&utm_targetid=dsa-473406585355&utm_loc_interest_ms=&utm_loc_physical_ms=9010670&gclid=EAIaIQobChMIg9DD_9zJ5gIVjp6fCh0tLgKlEAAYBCAAEgJFwvD_BwE
#this project helps to understand 5 main thing
#1) how to obtain data from yahoo or any finanicail wensite
#2) how to use pandas to put data in data frame
#3) how to merge two or more graphs using legend
#4) how to apply return formaula to graph
#5) how to open different graphs in different window

import pandas_datareader as pdr
import datetime
import pandas_datareader .data as web
import csv
import time
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl

seconds=time.time()
local_regular_time=time.ctime(seconds)

start = datetime.datetime(2019,1,1)
end= datetime.datetime(2019,12,20)
company="yahoo"
#stock="GOOGL"
stock="AAPL"
dataframe=web.DataReader(str(stock),str(company),start,end)
#stock=["GOOGL"]
#dataframe=web.DataReader(stock,str(company),start,end)

#entering data in data frame
dataframe.to_csv(str(local_regular_time))
dataframe.tail()

#creating a rolling mean
close_d=dataframe['Adj Close']
movingAverage=close_d.rolling(window=100).mean()
print(movingAverage)

# creating a graph for better understanding the effect of rolling mean
#creating a specific sizewindow
mpl.rc('figure',figsize=(9,8))
mpl.__version__

#deciding the style of matplotlib
style.use('ggplot')


close_d.plot(label='AAPL')
movingAverage.plot(label='MovingAvf')

#title="commpany "+company+" \n the stock "+stock
#plt.title(str(title))

    plt.legend()#showing two graphs in one for the comparision
plt.show()
#code understood from
#https://readthedocs.org/projects/pandas-datareader/downloads/pdf/latest/

#opening another window of matplotlib usually just change
#the number inside the plt.figure("any walue")
plt.figure(200)
rets = close_d / close_d.shift(1) - 1
rets.plot(label='return')
plt.show()