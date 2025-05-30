import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load data
df = pd.read_csv("streamlit/df_streamlit1.csv")

# Sidebar filters
st.sidebar.header("Filter Options")
sentiments = st.sidebar.multiselect("Select Sentiments", df["sentiment"].unique(), default=["improvement", "negative"])
category_options = df["category"].dropna().unique()
categories = st.sidebar.multiselect("Select Categories", category_options, default=category_options)

# Add confidence slider
max_conf = float(df["confidence"].max())
confidence_threshold = st.sidebar.slider("Minimum Confidence", min_value=0.75, max_value=max_conf, value=0.75, step=0.01)

filtered_df = df[
    (df["sentiment"].isin(sentiments)) &
    (df["category"].isin(categories)) &
    (df["confidence"] >= confidence_threshold)
]

# Overview
st.title("Customer Review Analysis Dashboard")
st.subheader("📊 Overview")
st.metric("Total Reviews", len(filtered_df))

# Category count chart
st.subheader("Feedback Count by Category")
fig, ax = plt.subplots()
sns.countplot(data=filtered_df, y="category", hue="sentiment", order=filtered_df["category"].value_counts().index, ax=ax)
st.pyplot(fig)

# WordCloud by feedback
st.subheader("Top Keywords in Feedback")
text = " ".join(filtered_df["feedback"].dropna())
wc = WordCloud(width=800, height=400, background_color="white").generate(text)
st.image(wc.to_array())

# Review table
st.subheader("📝 Filtered Reviews")
st.dataframe(filtered_df[["original_review", "sentiment", "category", "feedback", "confidence"]])

# Optional: download button
st.download_button("📥 Download Filtered CSV", filtered_df.to_csv(index=False), "filtered_reviews.csv")
