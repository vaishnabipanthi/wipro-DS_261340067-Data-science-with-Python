def convert_list_to_tuple():
    my_list = [1, 2, 3, 4, 5]
    print(f"Original list: {my_list} (Type: {type(my_list)})")
    
    my_tuple = tuple(my_list)
    print(f"Converted tuple: {my_tuple} (Type: {type(my_tuple)})")

if __name__ == "__main__":
    convert_list_to_tuple()