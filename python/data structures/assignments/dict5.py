def create_square_dict():
    square_dict = {}
    for i in range(1, 16):
        square_dict[i] = i * i
    
    print("Dictionary containing squares:")
    print(square_dict)

if __name__ == "__main__":
    create_square_dict()