
import streamlit as st
import pickle

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(
    page_title="SMS Spam Detection",
    page_icon="📩",
    layout="centered"
)

st.title("📩 SMS Spam Detection System")

st.write("Enter your SMS message below to check whether it is Spam or Not Spam.")

input_sms = st.text_area("Enter Your Message")

if st.button("Predict"):

    if input_sms.strip() == "":
        st.warning("Please enter a message first.")

    else:
        transformed_sms = tfidf.transform([input_sms])

        prediction = model.predict(transformed_sms)[0]

        if prediction == 1 or prediction == 'spam':
            st.error(" Spam Message Detected!")

        else:
            st.success(" This is Not a Spam Message.")
