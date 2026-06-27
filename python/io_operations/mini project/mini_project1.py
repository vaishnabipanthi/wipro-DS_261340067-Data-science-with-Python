import re
from collections import Counter

def find_secret_message():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            
        num_lines = len(lines)
        if num_lines == 0:
            print("File is empty.")
            return
            
        # Calculate meeting time based on number of lines
        time = num_lines
        period = "AM"
        if time == 12:
            period = "PM"
        elif time > 12 and time < 24:
            time -= 12
            period = "PM"
        elif time == 24:
            time = 12
            period = "AM"
            
        meeting_time = f"{time} {period}"
        
        # Calculate meeting place based on most frequent word
        content = " ".join(lines)
        # Extract words using regex
        words = re.findall(r'\b\w+\b', content)
        if not words:
            print("No words found.")
            return
            
        word_counts = Counter(w.lower() for w in words)
        most_common_word = word_counts.most_common(1)[0][0].title()
        
        meeting_place = f"{most_common_word} Street"
        
        print(f"Meeting time: {meeting_time}")
        print(f"Meeting place: {meeting_place}")
        
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    find_secret_message()