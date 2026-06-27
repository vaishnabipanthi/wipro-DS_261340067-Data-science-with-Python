def repeat_last_n():
    text = input("Enter a string: ")
    try:
        n = int(input("Enter an integer n: "))
        if 0 <= n <= len(text):
            result = text[-n:] * n if n > 0 else ""
            print(f"Output: {result}")
        else:
            print("n should be between 0 and the length of the string inclusive.")
    except ValueError:
        print("Invalid integer.")

if __name__ == "__main__":
    repeat_last_n()