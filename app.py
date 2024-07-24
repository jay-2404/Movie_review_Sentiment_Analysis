import pandas as pd
import pickle as pk
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

# Load model and scaler
model = pk.load(open('model.pkl', 'rb'))
scaler = pk.load(open('scaler.pkl', 'rb'))

# Title and description
st.title('Movie Review Sentiment Analysis')
st.write("""
    Welcome to the Movie Review Sentiment Analysis app! 
    Enter a movie review below and click 'Predict' to find out if the review is positive or negative.
""")

# Input form
with st.form(key='review_form'):
    review = st.text_area('Enter Movie Review', height=200)
    submit_button = st.form_submit_button('Predict')

# Prediction and result
if submit_button:
    if not review.strip():
        st.warning('Please enter a review before predicting.')
    else:
        # Transform and predict
        review_scale = scaler.transform([review]).toarray()
        result = model.predict(review_scale)

        # Display result
        st.subheader('Prediction Result')
        if result[0] == 0:
            st.markdown('<span style="color:red;">Negative Review</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span style="color:green;">Positive Review</span>', unsafe_allow_html=True)
