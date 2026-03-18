# 💰 Expense Tracker with ML Insights & Prediction

## 📌 Overview

This project is an end-to-end Machine Learning application that analyzes personal expense data and provides meaningful insights. It detects unusual spending patterns using anomaly detection, predicts future expenses, and presents results through an interactive and optimized dashboard.

---

## 🚀 Live App

👉 Try it here:  
https://expense-ml-project.streamlit.app

---

## 🚀 Features

- Upload expense CSV file
- Automated data preprocessing and feature engineering
- Anomaly detection using Isolation Forest
- Expense prediction using Machine Learning
- Insight generation:
  - Top spending category
  - Average spend
  - Total spend
  - Anomaly analysis
- Interactive charts (category-wise and time trends)
- Performance optimized using caching
- Clean modular architecture

---

## 🧠 Architecture

CSV → Data Processing → Feature Engineering → ML Models → Insights → Streamlit UI

---

## ⚡ Performance Optimization

To improve performance on deployment, caching has been implemented:

- Data Loading → @st.cache_data
- Data Processing → @st.cache_data
- Insights Generation → @st.cache_data
- Model Training → @st.cache_resource

### Benefits

- Faster app load times
- Avoids recomputation on every interaction
- Smooth user experience
- Production-ready behavior

---

## 🧠 Machine Learning Models

### 1. Anomaly Detection
- Model: Isolation Forest
- Detects unusual or high-value transactions

### 2. Expense Prediction
- Model: Random Forest Regressor
- Predicts expense based on:
  - Category
  - Day of week
  - Month

---

## 📁 Project Structure

expense-ml-project/

├── data/  
│   └── expenses.csv  

├── notebooks/  
│   └── eda.ipynb  

├── src/  
│   ├── data_processing.py   # Feature engineering  
│   ├── model.py             # ML models (anomaly + prediction)  
│   └── insights.py          # Insights & chart data  

├── app.py                   # Streamlit app (UI + caching)  
├── requirements.txt  
└── README.md  

---

## 🛠 Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
---

## 📊 Example Insights

- Identifies top spending category
- Calculates average and total spend
- Detects unusual transactions (anomalies)
- Visualizes category-wise and daily spending trends
- Predicts future expenses based on input features
- Visualizes:
  - Category-wise spending
  - Daily trends
  - Anomaly distribution

---

## 🎯 Use Case

This application helps users:

- Track their expenses effectively
- Identify abnormal spending behavior
- Forecast future expenses
- Gain insights into spending habits

---

## 💡 Future Improvements

- Improve prediction accuracy with additional features
- Add user authentication
- Connect to real-time data sources
- Store data in a database
- Add downloadable reports (PDF/Excel)

---

## 📬 Author

Built as part of a Machine Learning learning journey to demonstrate:

- End-to-end ML pipeline
- Model building & evaluation
- Deployment & performance optimization
- Production-ready architecture
