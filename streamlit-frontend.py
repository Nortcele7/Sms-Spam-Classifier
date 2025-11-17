import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

# Function to transform text
def transform_text(text):
    text = text.lower() # Converting into lowercase
    
    
    # Converting into tokens using nltk
    text = nltk.word_tokenize(text)
    y = []
    for items in text:
        if items.isalnum():
            y.append(items)

    text = y[:]  # List Cloning 
    y.clear()

    # Removing stop words and punctuation

    for items in text:
        if items not in stopwords.words('english') and items not in string.punctuation:
            y.append(items)

    text = y[:]
    y.clear()

    # Stemming 
    for items in text:
        y.append(ps.stem(items))
            
    return " ".join(y)


# Transforming the text 

if st.button("Predict"):

    transform_sms = transform_text(input_sms)

    vector_input = tfidf.transform([transform_sms])

    result = model.predict(vector_input)[0]

    if result==1:
        st.header("Spam")

    else:
        st.header("Not Spam")
