
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Explainability Dashboard")

importance = pd.DataFrame({

    "Feature": [
        "avg_rating",
        "avg_review_length",
        "review_count",
        "favorite_topic",
        "user_type"
    ],

    "Importance": [
        0.997,
        0.001,
        0.001,
        0.0006,
        0.0002
    ]
})

fig = px.bar(
    importance,
    x="Feature",
    y="Importance",
    title="Feature Importance for Rating Prediction"
)

st.plotly_chart(fig)

st.subheader("Evaluation Metrics")

st.metric(
    "RMSE",
    "0.3275"
)

st.metric(
    "NDCG@10",
    "1.0"
)

st.metric(
    "BERTScore F1",
    "0.938"
)

st.metric(
    "ROUGE-L",
    "0.40"
)
