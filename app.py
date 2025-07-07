import pandas as pd
import plotly.express as px
import streamlit as st

# reading data
car_data = pd.read_csv('vehicles.csv')

# setting a header 
st.header('Vehicles project')

# button to the histogram
hist_button = st.button('Create histogram')
    
if hist_button: # if the button is clicked
    # showing message
    st.write('Creating an histogram for the vehicles sales dataset')

    # histogram
    fig = px.histogram(car_data, x="odometer")
    
    # Plotly interactive chart
    st.plotly_chart(fig, use_container_width=True)

# button to the scatter plot
scat_button = st.button('Create scatter plot')

if scat_button: # if the button is clicked
    # showing message
    st.write('Creating an scatter plot for the vehicles sales dataset')

    # scatter plot
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Plotly interactive chart
    st.plotly_chart(fig, use_container_width=True)