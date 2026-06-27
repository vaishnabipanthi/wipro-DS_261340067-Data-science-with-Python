def cube_numbers():
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Using lambda function and map
    cubes = list(map(lambda x: x**3, list_1))
    
    print(f"Original list: {list_1}")
    print(f"Cubed list: {cubes}")

if __name__ == "__main__":
    cube_numbers()