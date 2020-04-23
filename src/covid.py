import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import stimation
from sklearn.linear_model import LinearRegression

routa = "csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

def print_country(dataset,country_name):
    countrypre = dataset.loc[country_name,:]
    #print(countrypre)
    country = countrypre["3/22/20":]
    country_pct = country.pct_change()
    #print(country)
    #print("percentatges"," ",country_name)
    #print(country_pct[-10:])
    country_pct.plot(label=str(country_name))
    return country, country_pct


def get_growth_factor(dataset,country_name):
    countrypre = dataset.loc[country_name,:]
    country = countrypre["3/22/20":]
    diferences = country.diff()

    print(diferences)
    print(diferences.fillna(0))
    for i in range(2,len(diferences)):
        # print("diferences ..",diferences.iloc[i-1]) 
        if diferences.iloc[i-1] != 0 :
            growth_factor = diferences.iloc[i] / diferences.iloc[i-1] 
            # print(" groth_factor :",diferences.iloc[i]," ",diferences.iloc[i-1])
            diferences.iat[i-1] = growth_factor

        # print("diferences iloc ",diferences.iloc[i], diferences.iloc[i-1] )
    growthfactor = diferences.iloc[:len(diferences)-1]
    print("diferences array")
    print(growthfactor)
    return growthfactor
    
#def print_projection(daset,dataset_pct,country_name):




    

timeseries = pd.read_csv(routa, index_col ="Country/Region")
print("printamos todo el DataSet")

dataitaly, dataitaly_pct = print_country(timeseries,'Italy')

#dataitaly, dataitaly_pct  i= print_country(pd.read_csv(routa, index_col ="Province/State"),'France')
dataspain, dataspain_pct = print_country(timeseries,'Spain')

#print_country(timeseries,'UK')

get_growth_factor(timeseries,'Spain')
get_growth_factor(timeseries,'Italy')




#print_country(timeseries,'South Korea')

plt.legend()
plt.show()

####################################
# linear_regressor = LinearRegression()
# xs = np.arange(7).reshape(1, -1)
# ys = dataspain_pct[-7:].values.reshape(1,-1)
# linear_regressor.fit(xs, ys) 
# Y_pred = linear_regressor.predict(np.array([0,1,2,3,4,5,6]))



# plt.plot(xs, Y_pred,color='blue', linewidth=3)
# plt.plot(np.arange(7), dataspain_pct[-7:])
# plt.plot(np.arange(7), Y_pred, color='red')


# plt.show()
###########################################

mediaspain = dataspain_pct[-2:].mean()
lastspain = dataspain.tail(1).iat[0]


print("Simulacion Spain ")

lstgeometric = stimation.stimation_geometric(mediaspain,lastspain)
lsttransala  = stimation.stimation_translation(dataitaly_pct[-7:].values,lastspain)

simulation = pd.DataFrame({"geometric":lstgeometric, "transaltaion":lsttransala})

print(simulation)
simulation.plot()
plt.show()

# for i in range(14):
#     x = x + x * mediaspain
#     print("adding")
#     print(x)
#     dataspain.append(x, ignore_index = True)

# print(dataspain.index)
# dataspain.plot()
# plt.show()








