import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def eda_mall_customers():
    # Note: To run this, download 'Mall_Customers.csv' from Kaggle
    try:
        # 1. Load Data
        df = pd.read_csv('Mall_Customers.csv')
        print("Data Loaded successfully. Shape:", df.shape)
        
        # 2. Basic Info & Statistics
        print("\n--- Dataset Info ---")
        print(df.info())
        print("\n--- Statistical Summary ---")
        print(df.describe())
        
        # 3. Univariate Analysis (Numerical)
        if 'Annual Income (k$)' in df.columns:
            plt.figure(figsize=(8, 5))
            sns.histplot(df['Annual Income (k$)'], kde=True, color='skyblue')
            plt.title('Distribution of Annual Income')
            plt.xlabel('Annual Income (k$)')
            plt.ylabel('Frequency')
            plt.show()
            
        # 4. Bivariate Analysis
        if 'Annual Income (k$)' in df.columns and 'Spending Score (1-100)' in df.columns:
            plt.figure(figsize=(8, 5))
            # Assuming 'Gender' exists for hue
            if 'Gender' in df.columns:
                sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Gender', data=df)
            else:
                sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', data=df)
            plt.title('Annual Income vs Spending Score')
            plt.show()
            
    except FileNotFoundError:
        print("Error: 'Mall_Customers.csv' not found. Please download from Kaggle.")

if __name__ == "__main__":
    eda_mall_customers()