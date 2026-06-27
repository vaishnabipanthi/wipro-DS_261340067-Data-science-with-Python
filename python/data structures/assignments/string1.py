def count_cases():
    text = input("Enter a string: ")
    upper_count = 0
    lower_count = 0
    
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")

if __name__ == "__main__":
    count_cases()