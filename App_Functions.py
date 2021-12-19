from numpy.lib.arraysetops import unique
import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

import streamlit as st
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


    # Condition 1{we are expensive and margin}
def helper(sector,data):
    # st.markdown("<h1 style='text-align: left; color: #64FF00;'>Margin </h1>", unsafe_allow_html=True)

    df1 = data[data['sector'] == sector].sort_values('fare',ascending = False)
    temp_df1 = df1.iloc[0,:]
    fare_is_more = df1.iloc[0,9]-df1.iloc[1,9]
    temp_df1["fare_is_more"] = fare_is_more
    return temp_df1
def test(data):
    alist =[]
    df2 = pd.DataFrame(columns = data.columns)  
    sectors = data['sector'].unique()
    for sector in sectors:
        temp = helper(sector,data)
        if(temp['FlightCode'][1:3]=='SG'):
            df2 = df2.append(temp)    
    result = df2.sort_values('fare_is_more',ascending = False).head(10)
    return result.drop(["Nun","DepTime","ArrivalTime","loadedby","LoadedOn","Departure_Date","Filename"],axis = 1).reset_index()
def PCA_Maker1(data):
    st.markdown("<h1 style='text-align: left; color: #64FF00;'>Amount by which fare is more</h1>", unsafe_allow_html=True)
    result =test(data)
    
    
    return result

#case2

def case2(data,sector):
    st.markdown("<h1 style='text-align: left; color: #64FF00;'>More Than Spicejet</h1>", unsafe_allow_html=True)

    df2 = pd.DataFrame(columns = data.columns) 
    unique_sector = data['sector'].unique()
    if sector not in unique_sector:
        return None
    df1 = data[data['sector'] == sector].sort_values('fare',ascending= False)
     
    for index,row in df1.iterrows():
        if row['FlightCode'][1:3]=="SG":
            print(row['FlightCode'][1:3])
            df2 = df2.drop(["Nun","DepTime","ArrivalTime","loadedby","LoadedOn","Departure_Date","Filename","Source"],axis = 1).reset_index()
            return df2.drop_duplicates('FlightCode')
            
        df2 = df2.append(row)
        
    return df2.drop_duplicates('FlightCode')
def PCA_Maker2(data,sector):
    result =case2(data,sector)
    return result

        

# case3
# New code before deployment
def case3(data,sector):
    st.markdown("<h1 style='text-align: left; color: #64FF00;'>Less Than Spicejet</h1>", unsafe_allow_html=True)

    df2 = pd.DataFrame(columns = data.columns) 
    unique_sector = data['sector'].unique()
    if sector not in unique_sector:
        return None
    df1 = data[data['sector'] == sector].sort_values('fare')
     
    for index,row in df1.iterrows():
        if row['FlightCode'][1:3]=="SG":
            print(row['FlightCode'][1:3])
            df2 = df2.drop(["Nun","DepTime","ArrivalTime","loadedby","LoadedOn","Filename","Source"],axis = 1).reset_index()
            return df2.drop_duplicates('FlightCode')

        df2 = df2.append(row)
        # print("appending")
    return df2.drop_duplicates('FlightCode')
def PCA_Maker3(data,sector):
    result =case3(data,sector)
    return result.head(10)

        # 


#Fare is more than spicejet
# def help(sector,data):
#     df1 = data[data['sector'] == sector].sort_values('fare',ascending = False)
#     temp_df1 = df1.iloc[0,:]
#     df3 =pd.DataFrame(columns = data.columns)
#     if(far)



    
  