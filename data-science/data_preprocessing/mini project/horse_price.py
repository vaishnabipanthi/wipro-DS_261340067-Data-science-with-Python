import pandas as pd

def house_price_preprocessing():
    # Use-Case: House Price Prediction
    try:
        # 1. Load the data in dataframe (Pandas)
        df = pd.read_csv('melb_data.csv')
        print("1. Data loaded successfully. Original Shape:", df.shape)
        
        # 2. Handle inappropriate data 
        # Example: Negative prices or zero rooms are illogical in a house price dataset
        if 'Price' in df.columns:
            df = df[df['Price'] > 0]
        if 'Rooms' in df.columns:
            df = df[df['Rooms'] > 0]
        print("2. Inappropriate data handled (filtered out invalid prices/rooms).")
        
        # 3. Handle the missing data
        # Fill numeric missing values with median (more robust to outliers than mean)
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        
        # Fill categorical missing values with the most frequent value (mode)
        cat_cols = df.select_dtypes(include=['object']).columns
        for col in cat_cols:
            df[col] = df[col].fillna(df[col].mode()[0])
        print("3. Missing data handled (Numerical -> median, Categorical -> mode).")
        
        # 4. Handle the categorical data
        # Using one-hot encoding (get_dummies) for categorical variables
        df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)
        print("4. Categorical data handled (One-hot encoding applied).")
        
        print("\nFinal processed shape ready for modeling:", df_encoded.shape)
        
    except FileNotFoundError:
        print("Error: 'melb_data.csv' not found. Please download it from Kaggle and place it in the directory.")

if __name__ == "__main__":
    house_price_preprocessing()