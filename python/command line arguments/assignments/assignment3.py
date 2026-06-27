import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes():
    if len(sys.argv) != 11:
        print("Usage: python assignment_3.py <num1> <num2> ... <num10>")
        return
        
    prime_sum = 0
    for arg in sys.argv[1:]:
        try:
            num = int(arg)
            if is_prime(num):
                prime_sum += num
        except ValueError:
            print(f"Ignoring invalid integer: {arg}")
            
    print(f"Sum of prime numbers: {prime_sum}")

if __name__ == "__main__":
    sum_of_primes()