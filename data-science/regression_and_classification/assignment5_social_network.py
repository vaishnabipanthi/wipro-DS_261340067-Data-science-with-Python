import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def predict_purchase():
    # Logistic Regression for Social_Network_Ads.csv
    try:
        df = pd.read_csv('Social_Network_Ads.csv')
        
        # Target column is 'Purchased'
        if 'Purchased' in df.columns:
            # Usually 'User ID' is irrelevant, and 'Gender' needs encoding
            if 'User ID' in df.columns:
                df = df.drop('User ID', axis=1)
                
            X = pd.get_dummies(df.drop('Purchased', axis=1), drop_first=True)
            y = df['Purchased']
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Standardizing features is important for Logistic Regression
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            
            model = LogisticRegression()
            model.fit(X_train_scaled, y_train)
            
            predictions = model.predict(X_test_scaled)
            print(f"Purchase Prediction Accuracy: {accuracy_score(y_test, predictions):.2f}")
            print(classification_report(y_test, predictions))
        else:
            print("Target column 'Purchased' not found.")
            
    except FileNotFoundError:
        print("Error: 'Social_Network_Ads.csv' not found.")

if __name__ == "__main__":
    predict_purchase()