import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np


from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def helper(sector,data):
    df1 = data[data['sector'] == sector].sort_values('fare',ascending = False)
    temp_df1 = df1.iloc[0,:]
    margin = df1.iloc[0,9]-df1.iloc[1,9]
    temp_df1["margin"] = margin
    return temp_df1
def test(data):
    alist =[]
    df2 = pd.DataFrame(columns = data.columns)  
    sectors = data['sector'].unique()
    for sector in sectors:
        temp = helper(sector,data)
        if(temp['FlightCode'][1:3]=='SG'):
            df2 = df2.append(temp)    
    result = df2.sort_values('margin',ascending = False).head(10)
    return result.drop(["Nun","DepTime","ArrivalTime","loadedby","LoadedOn","Departure_Date","Filename"],axis = 1).reset_index()
def PCA_Maker(data):
    result =test(data)
    return result


    
  