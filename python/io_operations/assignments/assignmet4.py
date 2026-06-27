def store_lines_in_list():
    filename = input("Enter filename: ")
    try:
        with open(filename, 'r') as f:
            lines_list = f.readlines()
        print(f"Successfully stored {len(lines_list)} lines into a list.")
        print("The list looks like:")
        print(lines_list)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    store_lines_in_list()