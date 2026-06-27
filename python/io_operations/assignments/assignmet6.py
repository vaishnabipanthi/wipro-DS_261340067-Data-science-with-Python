def count_word_frequency():
    filename = input("Enter filename: ")
    word_to_count = input("Enter word to count: ")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            # Split by whitespace to get words
            words = content.split()
            count = words.count(word_to_count)
            print(f"The word '{word_to_count}' appears {count} times.")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    count_word_frequency()