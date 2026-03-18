import pandas as pd

def preprocess_data(df):
    df['date'] = pd.to_datetime(df['date'])
    
    # Feature Engineering
    df['day_of_week'] = df['date'].dt.dayofweek
    df['month'] = df['date'].dt.month
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    
    # Encoding for anomaly model
    df_encoded = pd.get_dummies(df, columns=['category'])
    
    X = df_encoded.drop(['date', 'note'], axis=1)
    
    return df, X