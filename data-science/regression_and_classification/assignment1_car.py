import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def predict_car_price():
    # Multiple Linear Regression for cars.csv
    try:
        df = pd.read_csv('cars.csv')
        df = df.dropna() # Simple handling of missing values
        
        # Assume 'price' or 'Price' is the target variable
        target_col = 'price' if 'price' in df.columns else 'Price' if 'Price' in df.columns else None
        
        if target_col:
            # Handle categorical features via One-Hot Encoding
            X = pd.get_dummies(df.drop(target_col, axis=1), drop_first=True)
            y = df[target_col]
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            model = LinearRegression()
            model.fit(X_train, y_train)
            
            predictions = model.predict(X_test)
            print(f"Car Price Prediction (MSE): {mean_squared_error(y_test, predictions):.2f}")
            print(f"Car Price Prediction (R2): {r2_score(y_test, predictions):.2f}")
        else:
            print("Target column for price not found.")
            
    except FileNotFoundError:
        print("Error: 'cars.csv' not found.")

if __name__ == "__main__":
    predict_car_price()