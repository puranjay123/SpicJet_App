import streamlit as st
import pandas as pd
from App_Functions import PCA_Maker1,PCA_Maker2,PCA_Maker3

#widening the screen Display class
st.set_page_config(layout='wide')


col4 = st.sidebar
col4.header('Input Options')

# Slider sidebar
flight_time = col4.slider("Select the number of Flights",1,200,200)

scatter_col, settings_col = st.columns((4, 2))
scatter_col.title('Automated Analytical Tool ')

col1, mid, col2 = st.columns([2,1,1])
percent_timeframe = col4.selectbox('Choose the time Frame',['7d','24h','1h'])


# Browse files
settings_col.title('Browse Files')
uploaded_file = settings_col.file_uploader('Choose File')


def fun1():
    global uploaded_file
    if uploaded_file is  None:
        scatter_col.header('Please Choose a File')
        return 
    data = pd.read_csv(uploaded_file)
    result = PCA_Maker1(data)

    if(len(result)):
        # st.markdown("<h1 style='text-align: left; color: #64FF00;'>Less than SpiceJet</h1>", unsafe_allow_html=True)
        st.dataframe(result,width=1300, height=868)
    else:
        st.markdown("<h1 style='text-align: center; color: red;margin-right:100px;'>No Result Found</h1>", unsafe_allow_html=True) 
    # print("Hellow 1")
    
    
def fun2():
    global uploaded_file
    buff, col, buff2 = st.columns([3,1.5,0.0001])
    print("Hellow 2")
    form = col.form(key='my_form')
    my_sector = form.text_input(label='Enter the sector code')
    submit_button = form.form_submit_button(label='Submit')
    # cODITION
    
        # data = pd.read_csv(uploaded_file)
    if(submit_button) and my_sector!="":
        if uploaded_file is  None:
            scatter_col.header('Please Choose a File')
            return 
        data = pd.read_csv(uploaded_file)
        result = PCA_Maker2(data,my_sector)

        if(len(result)):
        # st.markdown("<h1 style='text-align: left; color: #64FF00;'>Less than SpiceJet</h1>", unsafe_allow_html=True)
            st.dataframe(result,width=1300, height=868)
    else:
        st.markdown("<h1 style='text-align: center; color: red;margin-right:100px;'>No Result Found</h1>", unsafe_allow_html=True)

    
   
        

def fun3():
    global uploaded_file
    buff, col, buff2 = st.columns([3,1.5,0.0001])
    print("Hellow 3")
    form = col.form(key='my_form')
    my_sector = form.text_input(label='Enter the sector code')
    submit_button = form.form_submit_button(label='Submit') 
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        if(submit_button) and my_sector!="":
            result = PCA_Maker3(data,my_sector)
            if(len(result)):
            # st.markdown("<h1 style='text-align: left; color: #64FF00;'>Less than SpiceJet</h1>", unsafe_allow_html=True)
                st.dataframe(result,width=1300, height=868)
        else:
            st.markdown("<h1 style='text-align: center; color: red;margin-right:100px;'>No Result Found</h1>", unsafe_allow_html=True)

    
    else:
        scatter_col.header('Please Choose a File')


# sELECT BOX
condition_flights = col4.selectbox('Available Tools',['Select the Tool','Margin','More than SG','Less than SG'])
# percent_dict = {"1":'sax',"2":'sexh',"3":'sexy'}
# selected_percent_timeframe = percent_dict[condition_flights]
if condition_flights == "Margin":
    fun1()
elif condition_flights == "More than SG":
    fun2()
elif condition_flights == "Less than SG":
    fun3() 



scatter_col, settings_col = st.columns((4, 2))

col1, mid, col2 = st.columns([2,1,1])



#Adding Sector column