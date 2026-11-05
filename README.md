# 📩 SMS Spam Detection System
### 🤖 Machine Learning | Natural Language Processing | Python | Streamlit

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Machine-Learning-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/NLP-Text%20Classification-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
</p>

<p align="center">
  <b>A Machine Learning-powered web application that intelligently detects whether an SMS message is SPAM or HAM (Legitimate Message).</b>
</p>

---

## 🌟 Project Overview

In today's digital world, SMS spam messages have become a common problem. Fraudulent messages, fake lottery notifications, phishing links, and unwanted advertisements can threaten users' privacy and security.

**SMS Spam Detection System** is a machine learning-based application designed to automatically classify text messages into two categories:

- 🚨 **SPAM:** Unwanted, promotional, fraudulent, or suspicious messages.
- ✅ **HAM:** Genuine and legitimate messages.

The system uses Natural Language Processing (NLP) and a trained Machine Learning model to analyze message content and predict its category.

With a simple and interactive Streamlit interface, users can enter any SMS message and instantly receive a prediction.

## 🎯 Key Features

- 🧠 **Machine Learning Classification:** Uses a trained ML model to identify spam and legitimate messages.
- 📝 **Real-Time Prediction:** Instantly analyzes user-entered SMS messages.
- 🔍 **Natural Language Processing:** Processes textual data for effective message classification.
- ⚡ **Interactive Web Interface:** Simple and user-friendly Streamlit application.
- 💾 **Pre-trained Model:** Loads the saved machine learning model using Pickle.
- 📊 **Data-Driven Learning:** Trained using an SMS spam dataset.
- 🛡️ **Spam Awareness:** Helps users identify potentially unwanted or fraudulent messages.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning model development |
| NLP | Text processing and classification |
| Pickle | Saving and loading the trained model |
| Streamlit | Interactive web application |
| Jupyter Notebook | Model training and experimentation |

## 🧠 How It Works

The application follows a Machine Learning pipeline:

1. **Dataset Collection:** Collect SMS messages labelled as spam or ham.
2. **Data Preprocessing:** Clean and prepare the textual data.
3. **Feature Extraction:** Convert text messages into numerical features using text vectorization.
4. **Model Training:** Train a machine learning classifier using the processed dataset.
5. **Model Serialization:** Save the trained model as `model.pkl`.
6. **Web Application:** Load the saved model into the Streamlit application.
7. **Prediction:** Accept a new SMS message and classify it as SPAM or HAM.

### 🔄 System Workflow

```text
       SMS Dataset
            |
            ▼
    Data Preprocessing
            |
            ▼
    Text Feature Extraction
            |
            ▼
    Model Training
            |
            ▼
     Trained ML Model
            |
            ▼
       model.pkl
            |
            ▼
    Streamlit Application
            |
            ▼
      User Input (SMS)
            |
            ▼
    Spam / Ham Prediction
            |
       ┌────┴────┐
       ▼         ▼
     SPAM       HAM
   🚨 Alert   ✅ Safe
```

## 📂 Project Structure

```text
SMS-Spam-Detection/
│
├── SMS SPAM detection.ipynb
│
├── app.py
│
├── model.pkl
│
├── requirement.txt
│
├── spam.csv
│
└── README.md
```

| File | Description |
|---|---|
| `SMS SPAM detection.ipynb` | Jupyter Notebook containing data preprocessing, model training, and evaluation. |
| `app.py` | Main Streamlit application for SMS classification. |
| `model.pkl` | Saved machine learning model used for predictions. |
| `requirement.txt` | List of required Python libraries. |
| `spam.csv` | Dataset containing labelled SMS messages. |
| `README.md
