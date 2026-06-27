def replace_last_value():
    sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    print(f"Sample list: {sample_list}")
    
    # Create a new list of tuples, replacing the last element of each tuple with 100
    expected_output = [t[:-1] + (100,) for t in sample_list]
    
    print(f"Expected Output: {expected_output}")

if __name__ == "__main__":
    replace_last_value()