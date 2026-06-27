import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def eda_social_network_ads():
    # Note: To run this, download 'Social_Network_Ads.csv' from Kaggle
    try:
        # 1. Load Data
        df = pd.read_csv('Social_Network_Ads.csv')
        print("Data Loaded successfully. Shape:", df.shape)
        
        # 2. Basic Info
        print("\n--- First 5 Rows ---")
        print(df.head())
        print("\n--- Statistical Summary ---")
        print(df.describe())
        
        # 3. EDA - Pairplot for numerical features
        # This will plot pairwise relationships and distribution of each feature
        print("\nGenerating Pairplot...")
        if 'Purchased' in df.columns:
            sns.pairplot(df, hue='Purchased', palette='Set2')
        else:
            sns.pairplot(df)
            
        plt.suptitle("Pairwise Relationships in Social Network Ads", y=1.02)
        plt.show()
        
    except FileNotFoundError:
        print("Error: 'Social_Network_Ads.csv' not found. Please download from Kaggle.")

if __name__ == "__main__":
    eda_social_network_ads()