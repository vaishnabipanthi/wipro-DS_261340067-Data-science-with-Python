def check_palindrome():
    text = input("Enter a string: ")
    # Optional: convert to lowercase and remove spaces for a more robust check
    # clean_text = text.replace(" ", "").lower()
    
    if text == text[::-1]:
        print(f"'{text}' is a Palindrome.")
    else:
        print(f"'{text}' is not a Palindrome.")

if __name__ == "__main__":
    check_palindrome()