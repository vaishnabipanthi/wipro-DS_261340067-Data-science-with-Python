def iterate_dict():
    my_dict = {'x': 100, 'y': 200, 'z': 300}
    
    print("Keys alone:")
    for key in my_dict:
        print(key)
        
    print("\nValues alone:")
    for value in my_dict.values():
        print(value)
        
    print("\nBoth keys and values:")
    for key, value in my_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    iterate_dict()