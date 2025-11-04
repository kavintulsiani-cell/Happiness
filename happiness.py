import streamlit as st
import plotly.express as ps


st.title = ("In Search for Happiness")
selection1 = st.selectbox  ("Select the data for the X-axis", "GDP", "Generosity", "Happiness")
selection2 = st.selectbox  ("Select the data for the Y-axis", "GDP", "Generosity", "Happiness")
st.subheader = {selection1} and {selection2}


fig = px.scatter (x = selection1, y = selection2)
st.plotly_chart(fig)