import pandas as pd

def pandas_exercise_3():
    # Note: To run this, download the cars dataset from:
    # https://archive.ics.uci.edu/ml/datasets/Auto+MPG
    # and save it as 'cars.csv' in the same directory.
    
    try:
        # a. Import Pandas (done above)
        # b. Import the Cars Dataset and store the Pandas DataFrame in the variable cars
        cars = pd.read_csv('cars.csv')
        
        # c. Inspect the first 10 Rows of the DataFrame cars
        print("--- First 10 Rows ---")
        print(cars.head(10))
        
        # d. Inspect the DataFrame cars by 'printing' cars
        print("\n--- DataFrame cars ---")
        print(cars)
        
        # e. Inspect the last 5 Rows
        print("\n--- Last 5 Rows ---")
        print(cars.tail(5))
        
        # f. Get some meta information on our DataFrame!
        print("\n--- Meta Information ---")
        cars.info()
        
    except FileNotFoundError:
        print("Error: 'cars.csv' not found. Please download the dataset and place it in the same directory.")

if __name__ == "__main__":
    pandas_exercise_3()