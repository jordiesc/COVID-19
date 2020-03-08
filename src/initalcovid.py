import pandas as pd
import matplotlib.pyplot as plt

routa = "csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"

timeseries = pd.read_csv(routa, index_col ="Country/Region")
print("printamos todo el DataSet")

print(timeseries)

print("filtraje Italia ")


#italiapre = timeseries.loc['Italy',:]
italiapre = timeseries.iloc[12,:]


print(italiapre)

italia = italiapre["1/22/20":]
print(italia)

print (italia.shape)
italia.pct_change().plot()
#italia.plot()
plt.show()






