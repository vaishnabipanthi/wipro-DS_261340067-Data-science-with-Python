import sys
import os

def display_welcome():
    if len(sys.argv) < 2:
        print("Usage: python assignment_2.py <welcome_message...>")
        return
        
    # The file name is the first argument in sys.argv
    file_name = os.path.basename(sys.argv[0])
    
    # The welcome message is the rest of the arguments
    welcome_message = " ".join(sys.argv[1:])
    
    print(f"File: {file_name}")
    print(f"Message: {welcome_message}")

if __name__ == "__main__":
    display_welcome()