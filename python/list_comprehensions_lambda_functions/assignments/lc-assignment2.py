def alphabet_dict():
    # Create a dictionary of 26 English alphabets mapped to their corresponding integer
    # Using comprehension where ASCII values map to 1-26
    # chr(97) is 'a', chr(122) is 'z'
    alpha_dict = {chr(i + 96): i for i in range(1, 27)}
    
    print("Alphabet mapped to integers:")
    print(alpha_dict)

if __name__ == "__main__":
    alphabet_dict()