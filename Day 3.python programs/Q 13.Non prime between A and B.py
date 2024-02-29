def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def non_prime_numbers_between_a_and_b(A, B):
    non_primes = [num for num in range(A, B+1) if not is_prime(num)]
    return non_primes

# Example usage:
A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))

result = non_prime_numbers_between_a_and_b(A, B)
print(f"Non-prime numbers between {A} and {B}: {result}")
