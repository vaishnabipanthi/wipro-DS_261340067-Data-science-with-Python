def read_first_n_lines():
    filename = input("Enter filename: ")
    try:
        n = int(input("Enter n (number of lines): "))
        with open(filename, 'r') as f:
            for i in range(n):
                line = f.readline()
                if not line: # End of file
                    break
                print(line, end='')
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid input for n. Please enter an integer.")

if __name__ == "__main__":
    read_first_n_lines()