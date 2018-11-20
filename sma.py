import matplotlib.pyplot as plt
import quandl
import pandas as pd

def SMA(sym, startDate, endDate):
	qcode="NSE/"+sym
	#get data Indiabulls price 
	data=quandl.get(qcode, authtoken="aCGwrfdPYgxEJqdd3B6q", start_date=startDate, end_date=endDate)

	#calculate moving average using pandas
	moving_avg = data.rolling(5).mean()
	print moving_avg

	#plot the moving average on a graph
	plt.plot(moving_avg)
	plt.show()
	return [expression]

#call OCHL with sample data
SMA("INFY", "2014-09-10", "2018-11-10")
