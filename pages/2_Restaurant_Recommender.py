
import streamlit as st
import pandas as pd

st.title("Restaurant Recommender")

data = pd.read_csv("sample_data.csv")

persona = st.selectbox(
    "Select User Persona",
    data["user_type_encoded"].unique()
)

topic = st.selectbox(
    "Preferred Dining Topic",
    data["topic_label"].unique()
)

filtered = data[
    (data["user_type_encoded"] == persona) &
    (data["topic_label"] == topic)
]

recommendations = (
    filtered.groupby("name")["stars_x"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

st.subheader("Recommended Restaurants")

for restaurant, rating in recommendations.items():
    st.write(
        f"⭐ {rating:.2f} — {restaurant}"
    )
