import streamlit as st
import pandas as pd

st.title("DEBUG MODE")

data = pd.read_csv("sample_data.csv")

st.write(data.columns.tolist())
