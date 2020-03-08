import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime  
from datetime import timedelta  

def stimation(likehood, date_time_str, initialvalue):
    print (datetime.now() + timedelta(days=1) ) 
    date_time_obj = datetime.datetime.strptime(date_time_str, '%m/%d/%y') 
    lst = []
    x = initialvalue
    df2 = pd.DataFrame()
    for i in range(14):
        x = x + x * likehod
        lst.append(x)
        print("adding")
        print(x)
        dataspain.append(x, ignore_index = True)