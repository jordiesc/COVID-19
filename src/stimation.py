import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime  
from datetime import timedelta  
from pandas import DataFrame
from sklearn.linear_model import LinearRegression




def stimation_geometric(df: DataFrame , likehood, initialvalue):
    # print (datetime.now() + timedelta(days=1) ) 
    lst = []
    x = initialvalue
    for i in range(7):
        x = x + x * likehood
        lst.append(x)
        df.loc[str(i)]=x
    return df


    
def stimation_geometric( likehood, initialvalue):
    lst = []
    x = initialvalue
    for i in range(7):
        x = x + x * likehood
        lst.append(x)
        
    return lst

def stimation_translation(likehood :[], initialvalue ):
    lst = []
    x = initialvalue
    for i in range(7):
        x = x + x * likehood[i]
        lst.append( x)  
    return lst

 




