import streamlit as st
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

from App_Functions import PCA_Maker

st.set_page_config(layout='wide')
scatter_col, settings_col = st.columns((4, 1))

scatter_col.title('List of the top 10 sectors where we are expensive than competition by most margin ')
settings_col.title('Browse Files')

uploaded_file = settings_col.file_uploader('Choose File')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    result = PCA_Maker(data)
    st.dataframe(result)
    
else:
    scatter_col.header('Please Choose a File')