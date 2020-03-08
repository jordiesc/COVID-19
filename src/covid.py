import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

routa = "csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"

def print_country(dataset,country_name):
    countrypre = dataset.loc[country_name,:]
    #print(countrypre)
    country = countrypre["1/22/20":]
    country_pct = country.pct_change()
    #print(country)
    #print(country_pct)
    country_pct.plot(label=str(country_name))
    return country, country_pct
    
#def print_projection(daset,dataset_pct,country_name):




    

timeseries = pd.read_csv(routa, index_col ="Country/Region")
print("printamos todo el DataSet")

print_country(timeseries,'Italy')
dataspain, dataspain_pct = print_country(timeseries,'Spain')
print_country(timeseries,'UK')
print_country(timeseries,'South Korea')

plt.legend()
plt.show()


print(" pintamos los españa")


mediaspain = dataspain_pct[-5:].mean()
lastspain = dataspain.tail(1)

print(dataspain)
print("ultimo elemento español")

x = lastspain

for i in range(14):
    x = x + x * mediaspain
    print("adding")
    print(x)
    dataspain.append(x, ignore_index = True)

print(dataspain)
dataspain.plot()
plt.show()






