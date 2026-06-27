def print_tuple_elements():
    # Need a tuple with at least 8 elements to safely print 4th from first and last
    my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    
    print(f"Tuple: {my_tuple}")
    # 4th element from first (index 3)
    print(f"4th element from first: {my_tuple[3]}")
    # 4th element from last (index -4)
    print(f"4th element from last: {my_tuple[-4]}")

if __name__ == "__main__":
    print_tuple_elements()