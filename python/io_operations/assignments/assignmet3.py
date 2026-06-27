def append_to_file():
    filename = input("Enter filename: ")
    text_to_append = input("Enter text to append: ")
    
    with open(filename, 'a') as f:
        f.write(text_to_append + '\n')
    print(f"Text successfully appended to {filename}.")

if __name__ == "__main__":
    append_to_file()