import pandas as pd
import matplotlib.pyplot as plt
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


    
    # numerical_col_list = []
    # categorical_col_list = []

    # for i in data.columns:
    #     if data[i].dtype == np.dtype('float64') or data[i].dtype == np.dtype('int64'):
    #         numerical_col_list.append(data[i])
    #     else:
    #         categorical_col_list.append(data[i])

    # numerical_data = pd.concat(numerical_col_list, axis=1)
    # categorical_data = pd.concat(categorical_col_list, axis=1)

    # numerical_data = numerical_data.apply(lambda x: x.fillna(np.mean(x)))

    # # Scaler
    # scaler = StandardScaler()
    # scaled_values = scaler.fit_transform(numerical_data)

    # pca = PCA() # PCA Object
    # pca_data = pca.fit_transform(scaled_values)
    # pca_data = pd.DataFrame(pca_data)

    # new_col_values = ['PCA_' + str(i) for i in range(1, len(pca_data.columns) + 1)]
    # col_mapper = dict(zip(list(pca_data.columns), new_col_values))
    # pca_data = pca_data.rename(columns=col_mapper)

    # output = pd.concat([data, pca_data], axis=1)
    # return output, list(categorical_data.columns), new_col_values