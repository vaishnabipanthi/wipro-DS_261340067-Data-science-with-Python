import re

def split_sentence():
    sentence = "A, very   very; irregular_sentence"
    
    # Split by any sequence of semicolons, commas, spaces, or underscores
    words = re.split(r'[;,\s_]+', sentence)
    
    # Join the words with a single space
    output = " ".join([w for w in words if w])
    print(f"Expected output : {output}")

if __name__ == "__main__":
    split_sentence()