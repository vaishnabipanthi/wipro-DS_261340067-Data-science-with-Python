def check_tuple_element():
    my_tuple = ('apple', 'banana', 'cherry', 'date')
    element = 'cherry'
    
    if element in my_tuple:
        print(f"'{element}' exists in the tuple.")
    else:
        print(f"'{element}' does not exist in the tuple.")

if __name__ == "__main__":
    check_tuple_element()