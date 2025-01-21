import streamlit as st
import pandas as pd
from sentiment_model import analyze_sentiment

# App title
st.title("Customer Sentiment Analysis")

# Sidebar inputs
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Process uploaded file
if uploaded_file:
    st.sidebar.success("File uploaded successfully!")
    data = pd.read_csv(uploaded_file)
    
    # Display uploaded data
    st.subheader("Uploaded Data")
    st.write(data.head())
    
    # Check for text column
    if 'review' in data.columns:
        st.subheader("Analyzing Sentiments")
        data['Sentiment'] = data['review'].apply(analyze_sentiment)
        st.write(data[['review', 'Sentiment']])
        
        # Sentiment counts
        st.subheader("Sentiment Distribution")
        st.bar_chart(data['Sentiment'].value_counts())
    else:
        st.warning("The uploaded file must contain a 'review' column.")
else:
    st.sidebar.info("Please upload a CSV file to proceed.")
