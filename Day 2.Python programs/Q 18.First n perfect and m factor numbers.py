def is_perfect_number(num):
    factors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)

    return sum(factors) == num, factors

def print_perfect_numbers_and_factors(n, m):
    count = 0
    num = 1

    while count < n:
        is_perfect, factors = is_perfect_number(num)
        if is_perfect:
            print(f"First {m} factors of {num} are: {', '.join(map(str, factors[:m]))}")
            count += 1
        num += 1

N =eval(input("Enter N element: "))
M =eval(input("Enter M element: "))

# Output
print_perfect_numbers_and_factors(N, M)
