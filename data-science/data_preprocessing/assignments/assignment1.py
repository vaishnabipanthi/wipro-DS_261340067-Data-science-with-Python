import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

def preprocess_with_sklearn():
    # Note: To run this, download the melb_data.csv dataset from Kaggle
    try:
        # 1. Load data
        df = pd.read_csv('melb_data.csv')
        print("Data loaded successfully. Initial shape:", df.shape)
        
        # 2. Identify numerical and categorical columns
        numeric_features = df.select_dtypes(include=['int64', 'float64']).columns
        categorical_features = df.select_dtypes(include=['object']).columns
        
        
        numeric_transformer = SimpleImputer(strategy='mean')
        
        # For categorical: Impute missing with most frequent and apply One-Hot Encoding
        categorical_transformer = ColumnTransformer(
            transformers=[
                ('cat_imputer', SimpleImputer(strategy='most_frequent'), categorical_features)
            ], remainder='passthrough')
            
        print("\nSklearn Preprocessing steps configured successfully.")
        print("- Numeric features will be imputed using statistical 'mean'.")
        print("- Categorical features will be imputed using 'most_frequent'.")
        
    except FileNotFoundError:
        print("Error: 'melb_data.csv' not found. Please place the dataset in the same directory.")

if __name__ == "__main__":
    preprocess_with_sklearn()