def find_tuple_index():
    my_tuple = (10, 20, 30, 40, 50)
    item_to_find = 30
    
    index = my_tuple.index(item_to_find)
    print(f"The index of {item_to_find} is {index}")

if __name__ == "__main__":
    find_tuple_index()