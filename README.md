# 🫀 Heart Disease Risk Prediction App

An end-to-end machine learning web application that predicts the risk of heart disease using user input health parameters.

Built with **Python**, trained in **Jupyter Notebook**, and deployed as an interactive web interface using **Streamlit**.

---

## 🚀 Demo

🔗 [Launch the App](https://heart-ml-a9gqfohr4qcvhheiqfuqvx.streamlit.app/) 

---

## 🧠 Overview

This app takes key health indicators such as age, blood pressure, cholesterol levels, and more to predict whether an individual is at **high or low risk** of heart disease using a **K-Nearest Neighbors (KNN)** classifier.

---

## 📌 Features

- 🧾 Interactive form to collect health metrics
- 🧠 Real-time machine learning predictions
- 🛠️ Preprocessing pipeline consistent with training (encoding + scaling)
- ✅ Intuitive and clean UI via Streamlit
- 💾 Model and scaler loading using Joblib

---

## 🧰 Tech Stack

| Task               | Tools / Libraries                         |
|--------------------|-------------------------------------------|
| Data Handling      | `Pandas`, `NumPy`                         |
| Visualization      | `Matplotlib`, `Seaborn` (in notebook)     |
| Model Building     | `scikit-learn` (KNN Classifier)           |
| Preprocessing      | `One-Hot Encoding`, `StandardScaler`      |
| Saving Model       | `joblib`                                  |
| Frontend App       | `Streamlit`                               |

---

## 🧪 Model Training (Jupyter Notebook)

- Cleaned and explored the dataset
- Categorical features encoded using **one-hot encoding**
- Features scaled using **StandardScaler**
- Trained a **K-Nearest Neighbors** classifier
- Evaluated with metrics like accuracy, confusion matrix
- Saved:
  - `KNN_HEART.pkl` – trained model
  - `scaler.pkl` – fitted scaler
  - `columns.pkl` – list of expected columns

---

## 🌐 Streamlit App 

- UI collects inputs using sliders and selectboxes
- Dynamically builds one-hot encoded input DataFrame
- Adds any missing columns to match training structure
- Scales data with pre-fitted scaler
- Predicts using loaded model
- Displays results in real-time (Low Risk / High Risk)

---
https://heart-ml-a9gqfohr4qcvhheiqfuqvx.streamlit.app/

