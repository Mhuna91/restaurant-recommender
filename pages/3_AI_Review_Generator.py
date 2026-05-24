
import streamlit as st
import random

st.title("AI Review Generator")

persona = st.selectbox(
    "User Persona",
    [
        "Harsh Critic",
        "Generous Reviewer",
        "Detailed Reviewer",
        "Casual Reviewer"
    ]
)

restaurant = st.text_input(
    "Restaurant Name"
)

cuisine = st.selectbox(
    "Cuisine Type",
    [
        "Mexican",
        "Pizza",
        "Sushi",
        "Coffee",
        "Burger",
        "Breakfast"
    ]
)

if st.button("Generate Review"):

    reviews = {

        "Harsh Critic":
        f"The {cuisine.lower()} experience at {restaurant} was disappointing. Food quality and service consistency require significant improvement.",

        "Generous Reviewer":
        f"I absolutely loved the {cuisine.lower()} dishes at {restaurant}. The atmosphere was welcoming and the staff were excellent.",

        "Detailed Reviewer":
        f"{restaurant} provided a memorable dining experience with balanced flavors, strong presentation quality, and attentive customer service.",

        "Casual Reviewer":
        f"Pretty nice place overall. Enjoyed the {cuisine.lower()} food at {restaurant}."
    }

    ratings = {

        "Harsh Critic":
        round(random.uniform(1.5,3.0),1),

        "Generous Reviewer":
        round(random.uniform(4.0,5.0),1),

        "Detailed Reviewer":
        round(random.uniform(3.5,4.8),1),

        "Casual Reviewer":
        round(random.uniform(3.0,4.2),1)
    }

    st.subheader("Predicted Rating")

    st.write(
        f"⭐ {ratings[persona]}"
    )

    st.subheader("Generated Review")

    st.write(
        reviews[persona]
    )
