def repeat_first_two():
    text = input("Enter a string (length >= 2): ")
    if len(text) >= 2:
        n = len(text)
        result = text[:2] * n
        print(f"Output: {result}")
    else:
        print("String length should be at least 2.")

if __name__ == "__main__":
    repeat_first_two()