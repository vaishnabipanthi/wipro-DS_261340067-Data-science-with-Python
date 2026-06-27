def ispalindrome(name):
    # Depending on requirements, we can make it case insensitive but constraint says completely in upper or lower case
    return name == name[::-1]

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in name if char in vowels)
    return count

def frequency_of_letters(name):
    freq = {}
    for char in name:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq