def set_intersection():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    intersection_set = set1.intersection(set2)
    # Alternatively: intersection_set = set1 & set2
    
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Intersection of sets: {intersection_set}")

if __name__ == "__main__":
    set_intersection()