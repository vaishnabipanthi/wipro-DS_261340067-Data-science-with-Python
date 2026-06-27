import numpy as np

def numpy_exercise_1():
    # Create two dimensional 3*3 array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    print(f"Array:\n{arr}")
    print(f"Number of dimensions (ndim): {arr.ndim}")
    print(f"Shape: {arr.shape}")
    
    # Slicing operation: get first 2 rows and last 2 columns
    sliced_arr = arr[:2, 1:]
    print(f"Sliced Array (first 2 rows, last 2 columns):\n{sliced_arr}")

if __name__ == "__main__":
    numpy_exercise_1()