import sys

def calculate_happiness():
    # sys.argv contains the script name as the first argument. 
    # The 3 strings should be arguments 1, 2, and 3.
    if len(sys.argv) != 4:
        print("Usage: python mini_project_1.py <string1> <string2> <string3>")
        return
        
    string1 = sys.argv[1].split('-')
    string2 = sys.argv[2].split('-')
    string3 = sys.argv[3].split('-')
    
    # Using sets for O(1) lookup times
    likes = set(string1)
    dislikes = set(string2)
    
    happiness = 0
    for num in string3:
        if num in likes:
            happiness += 1
        elif num in dislikes:
            happiness -= 1
            
    print(happiness)

if __name__ == "__main__":
    calculate_happiness()