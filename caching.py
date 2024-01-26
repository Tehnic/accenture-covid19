import streamlit as st
import getData as gd
import pandas as pd


@st.cache
def getTotalCasesByCountry():
    getTotalCasesByCountry().to_csv("data/total_cases_by_country.csv", index=False)
    return gd.getTotalCasesByCountry()

@st.cache
def trigger():
    try:
        df = pd.read_csv("data/total_cases_by_country.csv")
    except:
        df = getTotalCasesByCountry()
    return df