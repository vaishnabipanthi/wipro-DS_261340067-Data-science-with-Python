def remove_element():
    my_list = [10, 20, 30, 20, 40]
    element = 20
    print(f"Original list: {my_list}")
    my_list.remove(element)
    print(f"List after removing first occurrence of {element}: {my_list}")

if __name__ == "__main__":
    remove_element()