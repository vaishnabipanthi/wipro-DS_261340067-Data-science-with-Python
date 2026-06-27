def check_prime():
    try:
        num = int(input("Enter a number: "))
        if num <= 1:
            print(f"{num} is not a prime number.")
            return
        
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
                
        if is_prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
            
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    check_prime()