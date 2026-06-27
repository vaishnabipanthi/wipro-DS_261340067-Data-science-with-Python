def prepend_list():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(f"list1: {list1}")
    print(f"list2: {list2}")
    
    # Appending items of list1 to list2 in the front means list2 becomes list1 + list2
    list2 = list1 + list2
    print(f"list2 after prepending list1: {list2}")

if __name__ == "__main__":
    prepend_list()