import streamlit as st
import pandas as pd
import numpy as np
import time
import pydeck as pdk

#for mac users to bypass certificate error "invalidation"
import ssl
#for mac users to bypass certificate error "invalidation"
ssl._create_default_https_context = ssl._create_unverified_context

st.title("Covid Vaccine")

url_csv = ('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.ortho-max.net/wp-content/uploads/2018/01/Medical-Background-5.jpg")
    }

    </style>
    """,
    unsafe_allow_html=True
)

#define function that loads in data with specified number of rows
def load_data():
    data = pd.read_csv(url_csv)

    return data


#load data
data = load_data()


st.subheader('Number of People Vaccinated per 100')
st.line_chart(data.people_fully_vaccinated_per_hundred)


state_vacs_csv = ('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv')
state_data = pd.read_csv(state_vacs_csv)
lat_lon = pd.read_csv("./statelatlong.csv")
lat_lon = lat_lon.drop(columns='State')
lat_lon = lat_lon.rename(columns={"City": "State"})
joined_data = pd.merge(left=state_data, right=lat_lon, how='left', left_on='location', right_on='State')

state_data['total_distributed'].dropna(inplace = True)
state_data['total_distributed'].unique()
st.dataframe(data=joined_data, width=None, height=None)

chart_data = joined_data[['date','total_distributed','total_vaccinations','Latitude','Longitude']].copy()
chart_data = chart_data.loc[chart_data['date'] == '2021-02-05']
chart_data.dropna(inplace = True)


st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=29.42,
         longitude=-98.49,
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=chart_data,
            get_position='[Longitude, Latitude]',
            radius=100000,
            elevation_scale=10000,
            elevation_range=[0, 2000],
            pickable=True,
            extruded=True,
         ),
        #  pdk.Layer(
        #      'ScatterplotLayer',
        #      data=chart_data,
        #      get_position='[Longitude, Latitude]',
        #      get_color='[200, 30, 0, 160]',
        #      get_radius=200,
        #  ),
     ],
 ))