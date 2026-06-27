import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def predict_cancer():
    # Logistic Regression for cancer.csv
    try:
        df = pd.read_csv('cancer.csv')
        df = df.dropna()
        
        # Assuming the target column is 'diagnosis' or 'target'
        target_col = 'diagnosis' if 'diagnosis' in df.columns else 'target' if 'target' in df.columns else None
        
        if target_col:
            X = pd.get_dummies(df.drop(target_col, axis=1), drop_first=True)
            y = df[target_col]
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            model = LogisticRegression(max_iter=1000)
            model.fit(X_train, y_train)
            
            predictions = model.predict(X_test)
            print(f"Cancer Prediction Accuracy: {accuracy_score(y_test, predictions):.2f}")
            print(classification_report(y_test, predictions))
        else:
            print("Target column for cancer not found.")
            
    except FileNotFoundError:
        print("Error: 'cancer.csv' not found.")

if __name__ == "__main__":
    predict_cancer()