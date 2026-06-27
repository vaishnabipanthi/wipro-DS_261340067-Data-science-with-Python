import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def predict_startups_profit():
    # Multiple Linear Regression for 50_startups.csv
    try:
        df = pd.read_csv('50_startups.csv')
        
        # Features & Target
        if 'Profit' in df.columns:
            X = pd.get_dummies(df.drop('Profit', axis=1), drop_first=True)
            y = df['Profit']
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            model = LinearRegression()
            model.fit(X_train, y_train)
            
            predictions = model.predict(X_test)
            print(f"50 Startups Profit Prediction (MSE): {mean_squared_error(y_test, predictions):.2f}")
            print(f"50 Startups Profit Prediction (R2): {r2_score(y_test, predictions):.2f}")
        else:
            print("Target column 'Profit' not found.")
            
    except FileNotFoundError:
        print("Error: '50_startups.csv' not found.")

if __name__ == "__main__":
    predict_startups_profit()