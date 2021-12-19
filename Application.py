# import streamlit as st
# import pandas as pd
# st.set_page_config(layout='wide')

# col4 = st.sidebar
# col4.header('Input Options')


# # Slider sidebar
# flight_time = col4.slider("Select the number of Flights",1,200,200)

# percent_timeframe = col4.selectbox('Choose the time Frame',['7d','24h','1h'])



# pd.options.mode.chained_assignment = None  # default='warn'

# from App_Functions import PCA_Maker1

# # col2,col3 = st.columns((2,1))
# scatter_col, settings_col = st.columns((4, 2))

# scatter_col.title('Automated Analytical Tool ')
# col1, mid, col2 = st.columns([2,1,1])

# # About panel
# expander_bar = st.expander("Instructions To use The Application")
# expander_bar.markdown("""Upload the CSV file""")


# # scatter_col.image('a.png', width=300)

# settings_col.title('Browse Files')

# uploaded_file = settings_col.file_uploader('Choose File')
# # user_input = st.text_input("Enter the Sector Code")
# buff, col, buff2 = st.columns([3,1.5,0.0001])

# # col.text_input('smaller text window:')

# form = col.form(key='my_form')
# my_sector = form.text_input(label='Enter the sector code')
# submit_button = form.form_submit_button(label='Submit')
# # print(my_sector)
# option = st.selectbox('What Do you want to visualize',('A', 'B', 'C'))
# # st.set_page_config(layout="wide")

# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
#     if(submit_button) and my_sector!="":
#         result = PCA_Maker1(data,my_sector)
#         if(len(result)):
#             # st.markdown("<h1 style='text-align: left; color: #64FF00;'>Less than SpiceJet</h1>", unsafe_allow_html=True)
#             st.dataframe(result,width=1300, height=868)
#         else:
#             st.markdown("<h1 style='text-align: center; color: red;margin-right:100px;'>No Result Found</h1>", unsafe_allow_html=True)
#     # else  :
#     #     scatter_col.markdown("Please Enter a Valid Sector !!!!")
    
# else:
#     scatter_col.header('Please Choose a File')