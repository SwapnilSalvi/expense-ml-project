# 💰 Expense Tracker with ML Insights & Prediction

## 📌 Overview

This project is an end-to-end Machine Learning application that analyzes personal expense data, detects unusual spending patterns, and predicts future expenses. It combines data processing, anomaly detection, and regression modeling into an interactive dashboard.

---

## 🚀 Features

* Upload expense CSV file
* Automated data preprocessing and feature engineering
* Anomaly detection using Isolation Forest
* Expense prediction using Random Forest Regressor
* Insight generation (top category, average spend, total spend)
* Interactive dashboard built with Streamlit
* Category-wise and time-based visualizations
* Clean modular architecture (separation of concerns)

---

## 🔮 Prediction Feature

The app allows users to predict future expenses based on:

* Category
* Day of the week
* Month

This is powered by a machine learning regression model trained on historical data.

---

## 🧠 Architecture

```id="y9d3d9"
CSV → Data Processing → Feature Engineering → ML Models (Anomaly + Prediction) → Insights → Streamlit UI
```

### Module Breakdown:

* `data_processing.py`
  Handles data cleaning and feature engineering (date, day, month, weekend flag)

* `model.py`

  * Anomaly detection using Isolation Forest
  * Expense prediction using Random Forest Regressor

* `insights.py`
  Generates business insights and prepares chart data

* `app.py`
  Streamlit UI for user interaction, visualization, and prediction

---

## 📁 Project Structure

```id="z3dq0o"
expense-ml-project/
│
├── data/
│   └── expenses.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── data_processing.py
│   ├── model.py
│   └── insights.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit

---

## ▶️ How to Run Locally

```bash id="v72m3x"
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌍 Live Demo

👉 https://expense-ml-project.streamlit.app

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

* Add model caching for performance optimization
* Improve prediction accuracy with more features
* Add user authentication
* Connect to real-time data sources
* Store data in a database

---

## 📬 Author

Built as part of a Machine Learning learning journey to demonstrate end-to-end project development, clean architecture, and deployment readiness.
