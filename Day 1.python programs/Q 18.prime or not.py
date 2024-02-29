def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

input_number = eval(input("enter any number: "))
result = is_prime(input_number)

print(f"The number {input_number} is prime: {result}")
