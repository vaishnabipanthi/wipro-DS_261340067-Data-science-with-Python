import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def predict_diabetes():
    # Dataset: PIMA Indians diabetes dataset
    try:
        df = pd.read_csv('diabetes.csv')
        print("Data loaded. Shape:", df.shape)
        
        # Features & Target (Assuming 'Outcome' is the target)
        if 'Outcome' in df.columns:
            X = df.drop('Outcome', axis=1)
            y = df['Outcome']
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Scale features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            
            # 1. Logistic Regression
            lr_model = LogisticRegression()
            lr_model.fit(X_train_scaled, y_train)
            lr_preds = lr_model.predict(X_test_scaled)
            
            print("\n--- Logistic Regression ---")
            print(f"Accuracy: {accuracy_score(y_test, lr_preds):.2f}")
            print("Confusion Matrix:\n", confusion_matrix(y_test, lr_preds))
            print("Classification Report:\n", classification_report(y_test, lr_preds))
            
            # 2. K-Nearest Neighbour
            knn_model = KNeighborsClassifier(n_neighbors=5)
            knn_model.fit(X_train_scaled, y_train)
            knn_preds = knn_model.predict(X_test_scaled)
            
            print("\n--- K-Nearest Neighbors ---")
            print(f"Accuracy: {accuracy_score(y_test, knn_preds):.2f}")
            print("Confusion Matrix:\n", confusion_matrix(y_test, knn_preds))
            print("Classification Report:\n", classification_report(y_test, knn_preds))
        else:
            print("Target column 'Outcome' not found in dataset.")
            
    except FileNotFoundError:
        print("Error: 'diabetes.csv' not found. Please download from Kaggle.")

if __name__ == "__main__":
    predict_diabetes()