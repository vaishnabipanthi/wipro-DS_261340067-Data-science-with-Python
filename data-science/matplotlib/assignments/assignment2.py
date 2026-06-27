import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def eda_salary_data():
    # Note: To run this, download 'salary_data.csv' from Kaggle
    try:
        # 1. Load Data
        df = pd.read_csv('salary_data.csv')
        print("Data Loaded successfully. Shape:", df.shape)
        
        # 2. Basic Info
        print("\n--- First 5 Rows ---")
        print(df.head())
        
        # 3. EDA - Scatter Plot (Bivariate Analysis)
        if 'YearsExperience' in df.columns and 'Salary' in df.columns:
            plt.figure(figsize=(8, 5))
            sns.scatterplot(x='YearsExperience', y='Salary', data=df, color='green', s=100)
            plt.title('Years of Experience vs Salary')
            plt.xlabel('Years of Experience')
            plt.ylabel('Salary')
            
            # Optional: Add a regression line
            sns.regplot(x='YearsExperience', y='Salary', data=df, scatter=False, color='red')
            
            plt.show()
            
    except FileNotFoundError:
        print("Error: 'salary_data.csv' not found. Please download from Kaggle.")

if __name__ == "__main__":
    eda_salary_data()