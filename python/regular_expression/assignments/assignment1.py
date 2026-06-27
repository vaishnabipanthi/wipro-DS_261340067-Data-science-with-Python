import re

def check_octal():
    strings = ['789', '123', '004']
    # Regex pattern: start of string, one or more digits from 0-7, end of string
    pattern = re.compile(r'^[0-7]+$')
    
    for s in strings:
        if pattern.match(s):
            print(f"'{s}' contains only octal digits.")
        else:
            print(f"'{s}' does NOT contain only octal digits.")

if __name__ == "__main__":
    check_octal()