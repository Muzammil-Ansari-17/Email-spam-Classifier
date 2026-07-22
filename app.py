import streamlit as st
import pickle


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('Model.pkl','rb'))

st.title("Email & SMS Spam Classifier")


input_sms = st.text_area("Enter the message ", height= 350)

st.dialog("write the sms")

if st.button("Predict", use_container_width=True):


    # 1. preprocess
    from preprocess import transform_text
    transform_sms = transform_text(input_sms)

    #  2. vectorize

    vector_input = tfidf.transform([transform_sms])

    #  3. predict

    result = model.predict(vector_input)[0]
    prob = model.predict_proba(vector_input)[0]

    #  4. Display

    if result == 1:
        st.error("Spam Message")
        st.write(f"Confidence : {prob[1] * 100:.2f} %")
    else:
        st.success("Not Spam")
        st.write(f"Confidence :  {prob[0] * 100:.2f} %")



print(type(model))