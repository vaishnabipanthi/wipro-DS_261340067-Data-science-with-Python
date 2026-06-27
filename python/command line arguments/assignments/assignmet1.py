import sys

def sum_two_numbers():
    if len(sys.argv) != 3:
        print("Usage: python assignment_1.py <num1> <num2>")
        return
    
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        print(f"Sum: {num1 + num2}")
    except ValueError:
        print("Please provide valid numbers.")

if __name__ == "__main__":
    sum_two_numbers()