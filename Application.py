import streamlit as st
import pandas as pd

from App_Functions import PCA_Maker

st.set_page_config(layout='wide')
scatter_col, settings_col = st.columns((4, 1))

scatter_col.title('List the top 10 sectors where we are expensive than competition by most margin ')
settings_col.title('Browse Files')

uploaded_file = settings_col.file_uploader('Choose File')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    result = PCA_Maker(data)
    st.dataframe(result)
    # categorical_variable = settings_col.selectbox('Variable Select', options=cat_cols)
    # categorical_variable2 = settings_col.selectbox('Second Variable  Select', options=cat_cols)

    # pca1 = settings_col.selectbox('First Principle Component', options=pca_cols, index=0)
    # pca_cols.remove(pca1)
    # pca2 = settings_col.selectbox('Second Principle Component', options=pca_cols)


    # scatter_col.plotly_chart(px.scatter(data_frame=pca_data, x=pca1, y=pca2, color=categorical_variable, template='simple_white', 
    #                          height=800, hover_data=[categorical_variable2]), use_container_width=True)

else:
    scatter_col.header('Please Choose a File')