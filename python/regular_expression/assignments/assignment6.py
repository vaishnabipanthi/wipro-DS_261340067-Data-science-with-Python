import re

def check_words():
    words = [
        "civic",
        "trust",
        "widows",
        "maximum",
        "museums",
        "aa",
        "as"
    ]
    
    # Regex matches start character ^(.), any characters .*, and same end character \1$
    pattern = re.compile(r'^(.).*\1$')
    
    matching_words = []
    for word in words:
        if pattern.match(word):
            matching_words.append(word)
            
    print("Words that begin and end with the same character:")
    for w in matching_words:
        print(w)

if __name__ == "__main__":
    check_words()