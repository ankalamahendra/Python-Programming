def power(x, n):
    return x**n

def add(x, n):
    return x + n

def subtract(x, n):
    return x - n

def multiply(x, n):
    return x * n

def divide(x, n):
    if n != 0:
        return x / n
    else:
        return "Error: Division by zero"

x = float(input("Enter the value of x: "))
n = float(input("Enter the value of n: "))

choice = input("Enter the operation (pow, add, sub, mul, div): ").lower()

result = 0
if choice == 'pow':
    result = power(x, n)
elif choice == 'add':
    result = add(x, n)
elif choice == 'sub':
    result = subtract(x, n)
elif choice == 'mul':
    result = multiply(x, n)
elif choice == 'div':
    result = divide(x, n)
else:
    print("Invalid choice")

print(f"Result of {choice}({x}, {n}): {result}")
