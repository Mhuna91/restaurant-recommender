import streamlit as st
import pandas as pd

st.title("Restaurant Recommender")

# LOAD DATA
data = pd.read_csv("sample_data.csv")
profiles = pd.read_csv("user_profiles.csv")

# CREATE PERSONAS DYNAMICALLY
def assign_persona(row):

    if row["avg_rating"] <= 2.5:
        return "Harsh Critic"

    elif row["avg_review_length"] > 600:
        return "Detailed Reviewer"

    elif row["avg_rating"] >= 4.5:
        return "Generous Reviewer"

    else:
        return "Casual Reviewer"

profiles["user_type"] = profiles.apply(
    assign_persona,
    axis=1
)

# USER PERSONA SELECTION
persona = st.selectbox(
    "Select User Persona",
    profiles["user_type"].unique()
)

# TOPIC SELECTION
valid_topics = profiles[
    profiles["favorite_topic"] != "Unknown"
]["favorite_topic"].dropna().unique()

topic = st.selectbox(
    "Preferred Dining Topic",
    valid_topics
)

# FILTER USERS BY PERSONA
selected_users = profiles[
    profiles["user_type"] == persona
]["user_id"]

# FILTER SAMPLE DATA
filtered = data[
    data["user_id"].isin(selected_users)
]

# TOPIC FILTER USING CATEGORIES
topic_mapping = {
    "Mexican Food Lovers": "Mexican",
    "Pizza Enthusiasts": "Pizza",
    "Craft Beer & Nightlife": "Bars|Beer",
    "Sushi & Japanese Cuisine": "Sushi|Japanese",
    "Burger & Fast Food Fans": "Burgers|Fast Food",
    "Breakfast & Brunch Lovers": "Breakfast|Brunch",
    "Coffee & Cafe Culture": "Coffee|Cafe",
    "Thai Cuisine": "Thai",
    "Chinese Cuisine": "Chinese",
    "Italian Cuisine": "Italian"
}
keyword = topic_mapping.get(topic, topic)

filtered = filtered[
    filtered["categories"]
    .astype(str)
    .str.contains(
        keyword,
        case=False,
        na=False
    )
]

# HANDLE EMPTY RESULTS
if filtered.empty:

    st.warning(
        "No recommendations found."
    )

else:

    recommendations = (
        filtered.groupby("name")["stars_y"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    st.subheader(
        f"Top Recommendations for {persona}"
    )

    for restaurant, rating in recommendations.items():

        st.write(
            f"⭐ {rating:.2f} — {restaurant}"
        )
