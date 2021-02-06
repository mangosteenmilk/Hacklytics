import streamlit as st
import pandas as pd
import numpy as np
import time


#for mac users to bypass certificate error "invalidation"
import ssl
#for mac users to bypass certificate error "invalidation"
ssl._create_default_https_context = ssl._create_unverified_context

st.title("Covid Vaccine")

url_csv = ('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')


#define function that loads in data with specified number of rows
def load_data():
    data = pd.read_csv(url_csv)

    return data

#load data
data = load_data()



st.subheader('Number of People Vaccinated per 100')
st.line_chart(data.people_fully_vaccinated_per_hundred)


st.subheader('Human Life Expectancy')
st.line_chart(data.life_expectancy)