import my_module

def test_module():
    name = input("Sample input: ")
    
    # Check palindrome
    if my_module.ispalindrome(name):
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")
        
    # Count vowels
    vowels_count = my_module.count_the_vowels(name)
    print(f"No of vowels: {vowels_count}")
    
    # Frequency
    freq = my_module.frequency_of_letters(name)
    # The output format shown is b-2, o-1
    freq_str = ", ".join([f"{k}-{v}" for k, v in freq.items()])
    print(f"Frequency of letters: {freq_str}")

if __name__ == "__main__":
    test_module()