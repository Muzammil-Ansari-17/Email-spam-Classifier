import streamlit as st
import pickle
from preprocess import transform_text

tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("Model.pkl", "rb"))

st.title("📧 Email & SMS Spam Classifier")

input_sms = st.text_area(
    "Enter the message",
    placeholder="Type or paste your Email/SMS here...",
    height=350
)

if st.button("Predict", use_container_width=True):

    if not input_sms.strip():
        st.warning("⚠ Please enter an Email or SMS message.")
        st.stop()

    transform_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transform_sms])

    result = model.predict(vector_input)[0]
    prob = model.predict_proba(vector_input)[0]
    confidence = prob[result] * 100

    if result == 1:
        st.error("Spam Message")
    else:
        st.success("Not Spam")

    st.progress(confidence / 100)
    st.write(f"**Confidence:** {confidence:.2f}%")

st.markdown("---")
st.caption("Developed by Muzammil Ahmed")