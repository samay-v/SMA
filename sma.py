import matplotlib.pyplot as plt
import quandl
import pandas as pd

#get data Indiabulls price 
data=quandl.get("NSE/IBULISL", authtoken="aCGwrfdPYgxEJqdd3B6q", start_date="2018-09-10", end_date="2018-11-10")

#calculate moving average using pandas
moving_avg = data.rolling(5).mean()
print moving_avg

#plot the moving average on a graph
plt.plot(moving_avg)
plt.show()