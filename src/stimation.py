import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime  
from datetime import timedelta  
from pandas import DataFrame



def stimation(df: DataFrame , likehood, initialvalue):
    print (datetime.now() + timedelta(days=1) ) 
    lst = []
    x = initialvalue
    for i in range(15):
        x = x + x * likehood
        lst.append(x)
        print(x)
        df.loc[str(i)]=x
    print(df)
    return df

    

df = DataFrame(columns=['casos'])
df = stimation(df,.2,100)

df.plot()
plt.show()
