def find_longest_word():
    filename = input("Enter filename: ")
    try:
        with open(filename, 'r') as f:
            words = f.read().split()
            if not words:
                print("File is empty.")
                return
            longest_word = max(words, key=len)
            print(f"The longest word is: {longest_word}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    find_longest_word()