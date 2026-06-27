def remove_from_index():
    my_list = [10, 20, 30, 40, 50]
    index = 2
    print(f"Original list: {my_list}")
    removed_item = my_list.pop(index)
    print(f"Removed item '{removed_item}' at index {index}.")
    print(f"List after removal: {my_list}")

if __name__ == "__main__":
    remove_from_index()