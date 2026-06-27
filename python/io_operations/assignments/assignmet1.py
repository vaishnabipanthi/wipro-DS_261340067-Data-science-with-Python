def read_entire_file():
    filename = input("Enter filename: ")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print("--- File Content ---")
            print(content)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    read_entire_file()