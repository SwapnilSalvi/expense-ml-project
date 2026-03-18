def generate_insights(df):
    insights = {}
    
    # Basic insights
    insights['top_category'] = df.groupby('category')['amount'].sum().idxmax()
    insights['avg_spend'] = df['amount'].mean()
    insights['total_spend'] = df['amount'].sum()
    
    # Anomalies
    anomalies = df[df['anomaly'] == -1]
    insights['anomaly_count'] = len(anomalies)
    insights['anomaly_by_category'] = anomalies['category'].value_counts()
    insights['anomalies_df'] = anomalies[['date', 'amount', 'category']]
    
    # 📊 Chart Data
    insights['category_spend'] = df.groupby('category')['amount'].sum().sort_values(ascending=False)
    insights['daily_spend'] = df.groupby('date')['amount'].sum()
    
    return insights