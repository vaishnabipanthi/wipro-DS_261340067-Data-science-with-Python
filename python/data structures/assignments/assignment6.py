def insert_item():
    my_list = [10, 20, 30, 40]
    print(f"Original list: {my_list}")
    # The second element is at index 1. Inserting before it means inserting at index 1.
    my_list.insert(1, 15)
    print(f"List after inserting 15 before the second element: {my_list}")

if __name__ == "__main__":
    insert_item()