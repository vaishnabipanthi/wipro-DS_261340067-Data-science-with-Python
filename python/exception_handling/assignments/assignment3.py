def print_file_title_case():
    filename = input("Enter file name: ")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content.title())
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print_file_title_case()