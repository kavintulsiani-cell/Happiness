import streamlit as st
import plotly.express as ps


st.title = ("In Search for Happiness")
selection1 = st.selectbox  ("Select the data for the X-axis", ("GDP", "Generosity", "Happiness")).lower()
selection2 = st.selectbox  ("Select the data for the Y-axis", ("GDP", "Generosity", "Happiness")).lower()
st.subheader (f"{selection1.upper()} and {selection2.upper()}")

import pandas as pd
df = pd.read_csv ("happy.csv")
if selection1 and selection2 :
    fig = ps.scatter (data_frame = df, x = selection1, y = selection2,
                  labels = {selection1 :selection1.upper(), selection2 : selection2.upper()})
    st.plotly_chart(fig)