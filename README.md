# 💰 Expense Tracker with ML Insights & Prediction

## 📌 Overview

This project is an end-to-end Machine Learning application that analyzes personal expense data, detects unusual spending patterns, and predicts future expenses. It combines data processing, anomaly detection, and regression modeling into a fast, interactive dashboard.

---

## 🚀 Features

* Upload expense CSV file
* Automated data preprocessing and feature engineering
* Anomaly detection using Isolation Forest
* Expense prediction using Random Forest Regressor
* Insight generation (top category, average spend, total spend)
* Interactive dashboard built with Streamlit
* Category-wise and time-based visualizations
* ⚡ Performance optimized using caching
* Clean modular architecture (separation of concerns)

---

## 🔮 Prediction Feature

The app allows users to predict future expenses based on:

* Category
* Day of the week
* Month

This is powered by a machine learning regression model trained on historical data.

---

## ⚡ Performance Optimization

To ensure fast performance (especially after deployment), caching is implemented:

* Data Loading → `@st.cache_data`
* Data Processing → `@st.cache_data`
* Insights Generation → `@st.cache_data`
* Model Training → `@st.cache_resource`

### Benefits

* Faster load times
* Avoids recomputation on every interaction
* Smooth user experience
* Production-ready behavior

---

## 🧠 Architecture

CSV → Data Processing → Feature Engineering → ML Models (Anomaly + Prediction) → Insights → Streamlit UI

---

## 📦 Module Breakdown

* `data_processing.py`
  Handles data cleaning and feature engineering (date, day, month, weekend flag)

* `model.py`

  * Anomaly detection using Isolation Forest
  * Expense prediction using Random Forest Regressor

* `insights.py`
  Generates business insights and prepares chart data

* `app.py`
  Streamlit UI for user interaction, visualization, prediction, and caching

---

## 📁 Project Structure

expense-ml-project/

├── data/
│   └── expenses.csv

├── notebooks/
│   └── eda.ipynb

├── src/
│   ├── data_processing.py
│   ├── model.py
│   └── insights.py

├── app.py
├── requirements.txt
└── README.md

---

## 🛠 Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit

---

## ▶️ How to Run Locally

pip install -r requirements.txt
streamlit run app.py

---

## 🌍 Live Demo

👉 [https://expense-ml-project.streamlit.app]

---

## 📊 Example Insights

* Identifies top spending category
* Calculates average and total spend
* Detects unusual transactions (anomalies)
* Visualizes category-wise and daily spending trends
* Predicts future expenses based on input features

---

## 🎯 Use Case

This application helps users:

* Track their expenses effectively
* Identify abnormal spending behavior
* Forecast future expenses
* Gain insights into spending habits

---

## 💡 Future Improvements

* Improve prediction accuracy with additional features
* Add user authentication
* Connect to real-time data sources
* Store data in a database
* Add downloadable reports (PDF/Excel)

---

## 📬 Author

Built as part of a Machine Learning learning journey to demonstrate:

* End-to-end ML pipeline
* Model building & evaluation
* Deployment & performance optimization
* Production-ready architecture
