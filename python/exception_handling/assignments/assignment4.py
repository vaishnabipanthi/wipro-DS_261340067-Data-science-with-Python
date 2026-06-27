def check_index():
    # List with 10 integers
    my_list = [15, -2, 7, 0, -42, 88, -1, 3, -10, 25]
    
    try:
        index = int(input("Enter an index (0-9): "))
        value = my_list[index]
        
        if value > 0:
            print(f"The number at index {index} is {value} and it is positive.")
        elif value < 0:
            print(f"The number at index {index} is {value} and it is negative.")
        else:
            print(f"The number at index {index} is {value} (zero).")
            
    except ValueError:
        print("Error: Please enter a valid integer index.")
    except IndexError:
        print("Error: Invalid index. Index must be between 0 and 9.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    check_index()