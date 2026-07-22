import streamlit as st
import pickle


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('Model.pkl','rb'))

st.title("Email/SMS_Spam_Classifier")


input_sms = st.text_input("Enter the message ")

st.dialog("write the sms")

if st.button("Predict"):
    # 1. preprocess
    from preprocess import transform_text
    transform_sms = transform_text(input_sms)

    #  2. vectorize

    vector_input = tfidf.transform([transform_sms])

    #  3. predict

    result = model.predict(vector_input)[0]

    #  4. Display

    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
