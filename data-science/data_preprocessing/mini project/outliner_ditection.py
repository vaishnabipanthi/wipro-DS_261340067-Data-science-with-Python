import pandas as pd
import numpy as np

def outlier_detection():
    # Make sure to have a datasetExample.csv file present in the same directory
    # containing numeric columns to test this script.
    
    try:
        # Load the data in the DataFrame.
        df = pd.read_csv('datasetExample.csv')
        print("Data loaded successfully.")
        
        # Select numeric columns for outlier detection
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        print("\nDetecting Outliers using IQR (Interquartile Range) method:")
        # Detection of Outliers
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Find values outside the bounds
            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            
            print(f"Column '{col}' has {len(outliers)} outliers.")
            if not outliers.empty:
                print(f"  Lower bound: {lower_bound:.2f}, Upper bound: {upper_bound:.2f}")
                print(f"  Outlier indices: {outliers.index.tolist()}")
                
    except FileNotFoundError:
        print("Error: 'datasetExample.csv' not found. Please provide the dataset file.")

if __name__ == "__main__":
    outlier_detection()