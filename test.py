import streamlit as st
import pandas as pd
import numpy as np
import time


#for mac users to bypass certificate error "invalidation"
import ssl
#for mac users to bypass certificate error "invalidation"
ssl._create_default_https_context = ssl._create_unverified_context

st.title("test title")

url_csv = ('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')


#define function that loads in data with specified number of rows
def load_data():
    data = pd.read_csv(url_csv)

    return data


'Updating data...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Gathering data {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

#load data
data = load_data()

'...and now we\'re done!'




st.subheader('Number of People Vaccinated per 100')
st.line_chart(data.people_fully_vaccinated_per_hundred)


st.line_chart(data.new_cases_smoothed)
