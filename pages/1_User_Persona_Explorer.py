
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("User Persona Explorer")

user_profiles = pd.read_csv("user_profiles.csv")

persona_counts = (
    user_profiles["user_type"]
    .value_counts()
    .reset_index()
)

persona_counts.columns = [
    "Persona",
    "Count"
]

fig = px.bar(
    persona_counts,
    x="Persona",
    y="Count",
    text="Count",
    title="Behavioral User Personas"
)

st.plotly_chart(fig)

st.subheader("Sample User Profiles")

st.dataframe(
    user_profiles.head(20)
)
