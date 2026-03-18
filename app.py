import streamlit as st
import pandas as pd

from src.data_processing import preprocess_data
from src.model import detect_anomalies, train_prediction_model, predict_expense
from src.insights import generate_insights

st.title("💰 Expense Tracker with ML Insights")

st.write("Upload your expense CSV file to analyze your spending.")

# Upload file
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Raw Data")
    st.dataframe(df)

    # Process data
    df, X = preprocess_data(df)

    # Model
    df['anomaly'] = detect_anomalies(X)

    # Insights
    insights = generate_insights(df)

    # Show insights
    st.subheader("📊 Insights")
    st.write(f"Top Spending Category: {insights['top_category']}")
    st.write(f"Average Spend: ₹{insights['avg_spend']:.2f}")
    st.write(f"Total Spend: ₹{insights['total_spend']}")
    st.write(f"Anomalies: {insights['anomaly_count']}")
    
    st.write("Anomalies by Category:")
    st.write(insights['anomaly_by_category'])

    # Show anomalies
    st.subheader("🚨 Anomalies")
    st.dataframe(insights['anomalies_df'])
    
    # Show charts
    st.subheader("📊 Spending by Category")
    st.bar_chart(insights['category_spend'])
    
    st.subheader("📈 Daily Spending Trend")
    st.line_chart(insights['daily_spend'])
    
    st.subheader("🚨 Anomaly Distribution")

    if not insights['anomaly_by_category'].empty:
        st.bar_chart(insights['anomaly_by_category'])
    else:
        st.write("No anomalies detected")
        
        
    st.subheader("🔮 Predict Expense")

    category = st.selectbox("Category", df['category'].unique())
    day = st.selectbox("Day of Week (0=Mon)", list(range(7)))
    month = st.selectbox("Month", list(range(1, 13)))

    model, columns, mae = train_prediction_model(df)

    st.write(f"Model MAE: {mae:.2f}")

    if st.button("Predict"):
        pred = predict_expense(model, columns, category, day, month)
        st.success(f"Estimated Expense: ₹{pred:.2f}")