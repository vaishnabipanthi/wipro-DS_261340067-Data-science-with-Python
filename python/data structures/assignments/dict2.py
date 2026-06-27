def concatenate_dicts():
    dic1 = {1:10, 2:20} 
    dic2 = {3:30, 4:40} 
    dic3 = {5:50, 6:60}
    
    new_dict = {}
    new_dict.update(dic1)
    new_dict.update(dic2)
    new_dict.update(dic3)
    
    print(f"Expected Result : {new_dict}")

if __name__ == "__main__":
    concatenate_dicts()