# Email/SMS Spam Classifier

A Machine Learning web application that classifies Email and SMS messages as **Spam** or **Not Spam** using **Natural Language Processing (NLP)** and a **Multinomial Naive Bayes** classifier. The application is built with **Python**, **Scikit-learn**, and **Streamlit**.

---

## 🚀 Features

* Detects whether an Email or SMS is **Spam** or **Not Spam**
* Text preprocessing using NLTK
* TF-IDF Vectorization
* Multinomial Naive Bayes Classification
* Interactive Streamlit web interface
* Fast and lightweight prediction

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Scikit-learn**
* **Pandas**
* **NumPy**
* **NLTK**
* **Pickle**

---

## 📂 Project Structure

```text
Email-spam-Classifier/
│
├── app.py                 # Streamlit web application
├── preprocess.py          # Text preprocessing function
├── vectorizer.pkl         # Saved TF-IDF Vectorizer
├── Model.pkl              # Trained Machine Learning model
├── spam.csv               # Dataset
├── requirements.txt
└── README.md
```

---

## 📖 How It Works

1. User enters an Email or SMS message.
2. The text is converted to lowercase.
3. The message is tokenized.
4. Special characters and stopwords are removed.
5. Words are stemmed using Porter Stemmer.
6. The cleaned text is transformed using the trained TF-IDF Vectorizer.
7. The trained Multinomial Naive Bayes model predicts whether the message is **Spam** or **Not Spam**.


![Uploading image.png…]()



---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Muzammil-Ansari-17/Email-spam-Classifier.git
```

### Navigate to the project

```bash
cd Email-spam-Classifier
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 📊 Machine Learning Workflow

```
Raw Email/SMS
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Multinomial Naive Bayes
      │
      ▼
Spam / Not Spam
```

---

## 🧹 Text Preprocessing

The preprocessing pipeline includes:

* Convert text to lowercase
* Tokenization
* Remove special characters
* Remove English stopwords
* Porter Stemming
* Reconstruct cleaned sentence

---

## 📚 Libraries Used

```text
streamlit
scikit-learn
pandas
numpy
nltk
pickle
```

---

## 🎯 Future Improvements

* Support multiple machine learning models
* Display prediction confidence score
* Add message history
* Improve UI/UX
* Deploy the application online
* Support multiple languages

---

## 👨‍💻 Author

**Muzammil Ansari**

* GitHub: [https://github.com/Muzammil-Ansari-17](https://github.com/Muzammil-Ansari-17)
* LinkedIn: [www.linkedin.com/in/muzammil-ahmed-ansari-570674263](http://www.linkedin.com/in/muzammil-ahmed-ansari-570674263)

---

## ⭐ If you found this project helpful, consider giving it a star!
