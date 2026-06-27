import re

def clean_tweet():
    tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0px0d cc: @garybernhardt #rstats'''
    
    # Remove URLs
    cleaned = re.sub(r'http\S+', '', tweet)
    # Remove mentions
    cleaned = re.sub(r'@\w+', '', cleaned)
    # Remove hashtags
    cleaned = re.sub(r'#\w+', '', cleaned)
    # Remove RT and cc (with optional colon)
    cleaned = re.sub(r'\bRT\b', '', cleaned)
    cleaned = re.sub(r'\bcc\b:?', '', cleaned)
    # Remove punctuations
    cleaned = re.sub(r'[^\w\s]', '', cleaned)
    
    # Remove extra spaces and strip leading/trailing whitespace
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    
    print(f"Desired output = '{cleaned}'")

if __name__ == "__main__":
    clean_tweet()