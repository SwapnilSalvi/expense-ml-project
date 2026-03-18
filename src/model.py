from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd

def detect_anomalies(X):
    model = IsolationForest(contamination=0.02, random_state=42)
    model.fit(X)
    
    return model.predict(X)


def train_prediction_model(df):
    # Features & target
    X = df[['category', 'day_of_week', 'month']]
    y = df['amount']
    
    # One-hot encoding
    X = pd.get_dummies(X, columns=['category'], drop_first=True)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Model
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    
    # Evaluation
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    
    return model, X.columns, mae


def predict_expense(model, columns, category, day_of_week, month):
        
    input_df = pd.DataFrame({
        'category': [category],
        'day_of_week': [day_of_week],
        'month': [month]
    })
    
    input_df = pd.get_dummies(input_df)
    
    # Align columns
    input_df = input_df.reindex(columns=columns, fill_value=0)
    
    prediction = model.predict(input_df)[0]
    
    return prediction