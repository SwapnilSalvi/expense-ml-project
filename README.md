# 💰 Expense Tracker with ML Insights

## 📌 Overview

This project is an end-to-end Machine Learning application that analyzes personal expense data and provides meaningful insights. It detects unusual spending patterns using anomaly detection and presents results through an interactive dashboard.

---

## 🚀 Features

* Upload expense CSV file
* Automated data preprocessing and feature engineering
* Anomaly detection using Isolation Forest
* Insight generation (top category, average spend, total spend)
* Interactive dashboard built with Streamlit
* Category-wise and time-based visualizations
* Clean modular architecture (separation of concerns)

---

## 🧠 Architecture

```
CSV → Data Processing → Feature Engineering → ML Model → Insights → Streamlit UI
```

### Module Breakdown:

* `data_processing.py`
  Handles data cleaning and feature engineering (date features, encoding)

* `model.py`
  Implements anomaly detection using Isolation Forest

* `insights.py`
  Generates business insights and prepares chart data

* `app.py`
  Streamlit UI for user interaction and visualization

---

## 📁 Project Structure

```
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

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Example Insights

* Identifies top spending category
* Calculates average and total spend
* Detects unusual transactions (anomalies)
* Visualizes category-wise and daily spending trends

---

## 🎯 Use Case

This application helps users:

* Track their expenses effectively
* Identify abnormal spending behavior
* Gain insights into spending habits

---

## 💡 Future Improvements

* Add expense prediction model
* Deploy application online
* Add user authentication
* Connect to real-time data sources

---

## 📬 Author

Built as part of a Machine Learning learning journey to demonstrate end-to-end project development and deployment readiness.