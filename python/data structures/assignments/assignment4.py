def count_occurrences():
    my_list = [1, 2, 3, 2, 4, 2, 5]
    element = 2
    count = my_list.count(element)
    print(f"The element {element} appears {count} times in the list {my_list}.")

if __name__ == "__main__":
    count_occurrences()