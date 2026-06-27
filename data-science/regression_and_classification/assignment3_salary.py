import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def predict_salary():
    # Simple Linear Regression for Salary_Data.csv
    try:
        df = pd.read_csv('Salary_Data.csv')
        
        # Features & Target
        if 'Salary' in df.columns and 'YearsExperience' in df.columns:
            # Reshape X for Simple Linear Regression
            X = df[['YearsExperience']]
            y = df['Salary']
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            model = LinearRegression()
            model.fit(X_train, y_train)
            
            predictions = model.predict(X_test)
            print(f"Salary Prediction (MSE): {mean_squared_error(y_test, predictions):.2f}")
            print(f"Salary Prediction (R2): {r2_score(y_test, predictions):.2f}")
        else:
            print("Required columns not found.")
            
    except FileNotFoundError:
        print("Error: 'Salary_Data.csv' not found.")

if __name__ == "__main__":
    predict_salary()