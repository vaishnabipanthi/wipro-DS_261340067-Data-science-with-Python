def remove_x():
    text = input("Enter a string: ")
    if not text:
        return
        
    start_idx = 0
    end_idx = len(text)
    
    if text[0] == 'x':
        start_idx = 1
    if len(text) > 1 and text[-1] == 'x':
        end_idx = -1
        
    result = text[start_idx:end_idx] if end_idx != -1 else text[start_idx:len(text)-1]
    
    # Handle single 'x' case properly
    if len(text) == 1 and text == 'x':
        result = ""
        
    print(f"Output: {result}")

if __name__ == "__main__":
    remove_x()