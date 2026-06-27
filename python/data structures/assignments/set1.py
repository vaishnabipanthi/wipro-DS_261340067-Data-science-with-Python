def remove_from_set():
    my_set = {10, 20, 30, 40, 50}
    item_to_remove = 30
    print(f"Original set: {my_set}")
    
    if item_to_remove in my_set:
        my_set.remove(item_to_remove)
        print(f"Set after removing {item_to_remove}: {my_set}")
    else:
        print(f"Item {item_to_remove} not found in set.")

if __name__ == "__main__":
    remove_from_set()
