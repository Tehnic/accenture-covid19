import streamlit as st
import getData as gd

st.set_page_config(page_title="COVID-19 Data Visualiser", page_icon="🦠", layout="wide", initial_sidebar_state="expanded")

st.pyplot(gd.getTotalCasesByCountry().any().plot(kind='bar', x='COUNTRY_REGION', y='TOTAL_CASES', title='Total cases by country'))
st.pyplot(gd.getTotalCasesByDate().any().plot(kind='line', x='DATE', y='TOTAL_CASES', title='Total cases by date'))
st.pyplot(gd.getTotalDeaths().any().plot(kind='bar', x='COUNTRY_REGION', y='TOTAL_DEATHS', title='Total deaths by country'))
country = st.text_input("Enter country name:", "Latvia")
st.pyplot(gd.getDeathsByCountry(country).any().plot(kind='line', x='DATE', y='DEATHS', title='Deaths by date in ' + country))

st.text("Marks Dvojeglazovs, Big Data Engineering bootcamp for Accenture, 2024")