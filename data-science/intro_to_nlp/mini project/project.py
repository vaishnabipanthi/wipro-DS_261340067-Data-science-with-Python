import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

def predict_rating():
    # Use Case: Rating Prediction using NLP
    try:
        # Load dataset
        df = pd.read_csv('yelp.csv')
        print("Data loaded. Shape:", df.shape)
        
        # Ensure text and stars columns exist
        if 'text' in df.columns and 'stars' in df.columns:
            # 1. Features (Text) and Labels (Stars)
            X = df['text']
            y = df['stars']
            
            # 2. Text Preprocessing & Vectorization
            # TF-IDF handles basic preprocessing like lowercasing and tokenization implicitly
            print("Vectorizing text using TF-IDF...")
            vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
            X_vectorized = vectorizer.fit_transform(X)
            
            # 3. Train Test Split
            X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)
            
            # 4. Build Model
            # Multinomial Naive Bayes is a strong baseline for text classification
            print("Training Multinomial Naive Bayes Model...")
            model = MultinomialNB()
            model.fit(X_train, y_train)
            
            # 5. Evaluate
            predictions = model.predict(X_test)
            print("\n--- Model Evaluation ---")
            print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")
            print(classification_report(y_test, predictions))
            
        else:
            print("Error: Required columns 'text' and 'stars' not found in the dataset.")
            
    except FileNotFoundError:
        print("Error: 'yelp.csv' not found. Please download from Kaggle.")

if __name__ == "__main__":
    predict_rating()