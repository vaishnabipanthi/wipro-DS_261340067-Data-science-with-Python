import pandas as pd
import string
import nltk  # type: ignore
from nltk.corpus import stopwords  # type: ignore
from nltk.stem import PorterStemmer  # type: ignore

def preprocess_text(text):
    # 1. Lowercase
    text = str(text).lower()
    
    # 2. Remove punctuation
    text = "".join([char for char in text if char not in string.punctuation])
    
    # 3. Tokenization (basic split, though nltk.word_tokenize is preferred)
    words = text.split()
    
    # 4. Remove stopwords
    try:
        stop_words = set(stopwords.words('english'))
    except LookupError:
        # Automatically download stopwords if missing
        nltk.download('stopwords')
        stop_words = set(stopwords.words('english'))
        
    words = [word for word in words if word not in stop_words]
        
    # 5. Stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    
    return " ".join(words)

def preprocess_spam_collection():
    try:
        # Load dataset
        # SMSSpamCollection is typically a tab-separated file without a header row
        df = pd.read_csv('SMSSpamCollection', sep='\t', names=['label', 'message'])
        print("Data loaded successfully. Shape:", df.shape)
        
        # Apply preprocessing
        print("Applying text preprocessing pipeline (lowercasing, punctuation removal, stopwords, stemming)...")
        df['processed_message'] = df['message'].apply(preprocess_text)
        
        # Display results
        print("\n--- Original vs Processed Messages ---")
        for i in range(5):
            print(f"Original:  {df['message'].iloc[i]}")
            print(f"Processed: {df['processed_message'].iloc[i]}\n")
            
    except FileNotFoundError:
        print("Error: 'SMSSpamCollection' file not found. Please download from Kaggle.")

if __name__ == "__main__":
    # Uncomment the following line if running for the first time to download stopwords
    # nltk.download('stopwords')
    preprocess_spam_collection()