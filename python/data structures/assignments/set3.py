def set_union():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    
    union_set = set1.union(set2)
    # Alternatively: union_set = set1 | set2
    
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union of sets: {union_set}")

if __name__ == "__main__":
    set_union()