# SMS Spam Classifier

A machine learning project that classifies SMS messages as spam or ham (not spam) using Natural Language Processing (NLP) and a Streamlit web interface.

## 🚀 Features

- **Machine Learning Model**: Trained classifier to detect spam messages
- **Text Processing**: Implements tokenization, stemming, and stopword removal
- **Interactive Web Interface**: User-friendly Streamlit application
- **Real-time Predictions**: Instant classification of SMS messages

## 📋 Prerequisites

- Python 3.7+
- pip (Python package installer)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Nortcele7/Sms-Spam-Classifier.git
cd Sms-Spam-Classifier
```

2. Install required packages:
```bash
pip install streamlit nltk pandas numpy scikit-learn
```

3. Download NLTK data:
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

## 📁 Project Structure

```
Email-Spam-Classifier/
├── email-sms-spam-classifier.ipynb  # Model training notebook
├── streamlit-frontend.py            # Streamlit web application
├── spam.csv                          # Dataset
├── vectorizer.pkl                    # TF-IDF vectorizer (generated)
├── model.pkl                         # Trained model (generated)
├── README.md                         # Project documentation
└── LICENSE                           # MIT License
```

## 🎯 Usage

1. **Train the Model** (if not already done):
   - Open and run `email-sms-spam-classifier.ipynb` to train the model
   - This will generate `vectorizer.pkl` and `model.pkl`

2. **Run the Streamlit App**:
```bash
streamlit run streamlit-frontend.py
```

3. **Classify Messages**:
   - Enter an SMS message in the text area
   - Click "Predict" to classify the message
   - View the result (Spam or Not Spam)

## 🧠 How It Works

1. **Text Preprocessing**:
   - Converts text to lowercase
   - Tokenizes the message
   - Removes non-alphanumeric characters
   - Removes stopwords and punctuation
   - Applies Porter Stemming

2. **Feature Extraction**:
   - Uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization

3. **Classification**:
   - Trained machine learning model predicts spam/ham

## 📊 Dataset

The project uses the SMS Spam Collection dataset (`spam.csv`) which contains labeled SMS messages for training and evaluation.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Nortcele7**
- GitHub: [@ShreyamRegmi/Nortcele7](https://github.com/Nortcele7)

## 🙏 Acknowledgments

- SMS Spam Collection Dataset
- NLTK library for NLP operations
- Streamlit for the web interface
- scikit-learn for machine learning tools

## 📧 Contact

For any questions or feedback, please open an issue on GitHub.

---

Made with ❤️ by Shreyam Regmi
