import pandas as pd

def preprocess_with_pandas():
    # Note: To run this, download the melb_data.csv dataset from Kaggle
    try:
        # 1. Load data
        df = pd.read_csv('melb_data.csv')
        print("Data loaded successfully. Initial shape:", df.shape)
        
        # 2. Handle missing data from a statistical perspective
        # Numerical: Fill missing values with the column mean
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        print("\nMissing numeric values filled with column statistical means.")
        
        # Categorical: Fill missing values with the column mode
        cat_cols = df.select_dtypes(include=['object']).columns
        for col in cat_cols:
            df[col] = df[col].fillna(df[col].mode()[0])
        print("Missing categorical values filled with modes.")
        
        # 3. Handle categorical data (One-Hot Encoding via pandas)
        df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
        print("\nCategorical data encoded using pd.get_dummies.")
        print("Final shape after pandas preprocessing:", df.shape)
        
    except FileNotFoundError:
        print("Error: 'melb_data.csv' not found. Please place the dataset in the same directory.")

if __name__ == "__main__":
    preprocess_with_pandas()