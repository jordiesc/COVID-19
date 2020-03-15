import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

routa = "csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"

def print_country(dataset,country_name):
    countrypre = dataset.loc[country_name,:]
    #print(countrypre)
    country = countrypre["1/22/20":]
    country_pct = country.pct_change()
    country_pct.plot(label=str(country_name))
    return country, country_pct


timeseries = pd.read_csv(routa, index_col ="Province/State")
print("printamos todo el DataSet")

print_country(timeseries,'Hubei')

plt.legend()
plt.show()