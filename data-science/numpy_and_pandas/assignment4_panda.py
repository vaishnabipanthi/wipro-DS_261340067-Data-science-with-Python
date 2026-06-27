import pandas as pd

def pandas_exercise_4():
    # Note: To run this, download the 50_startups dataset from:
    # https://www.kaggle.com/datasets/farhanmd29/50-startups
    # and save it as '50_startups.csv' in the same directory.
    
    try:
        # a. Create DataFrame using Pandas
        # b. Read the data from 50_startups.csv file and load the data into dataframe.
        df = pd.read_csv('50_startups.csv')
        
        # c. Check the statistical summary.
        print("--- Statistical Summary ---")
        print(df.describe())
        
        # d. Check for correlation coefficient between dependent and independent variables.
        # numeric_only=True ensures categorical variables like 'State' are ignored
        print("\n--- Correlation Coefficient Matrix ---")
        correlation = df.corr(numeric_only=True)
        print(correlation)
        
    except FileNotFoundError:
        print("Error: '50_startups.csv' not found. Please download the dataset and place it in the same directory.")

if __name__ == "__main__":
    pandas_exercise_4()