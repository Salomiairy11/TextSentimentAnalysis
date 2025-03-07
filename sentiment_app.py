import streamlit as st
import joblib

pipeline = joblib.load('nlp_kathford.joblib')

st.title("🎭 Sentiment Analysis App")
st.subheader("Enter a review below, and the model will predict whether it's Positive or Negative.")

user_input = st.text_area("Type your review here:")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        prediction = pipeline.predict([user_input])[0]
        sentiment = "😊 Positive" if prediction == 1 else "😢 Negative"
        st.markdown(f"### Sentiment: **{sentiment}**")
    else:
        st.warning("Please enter a review before clicking the button.")

st.markdown("---")
st.markdown("**Built with ❤️ using Streamlit**")
