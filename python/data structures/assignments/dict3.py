def check_key():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    key_to_check = 'b'
    
    if key_to_check in my_dict:
        print(f"Key '{key_to_check}' already exists in dictionary.")
    else:
        print(f"Key '{key_to_check}' does not exist.")

if __name__ == "__main__":
    check_key()