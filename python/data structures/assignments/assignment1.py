def list_basics():
    my_list = [10, 20, 30, 40, 50]
    print(f"List items: {my_list}")
    for i in range(len(my_list)):
        print(f"Element at index {i}: {my_list[i]}")

if __name__ == "__main__":
    list_basics()