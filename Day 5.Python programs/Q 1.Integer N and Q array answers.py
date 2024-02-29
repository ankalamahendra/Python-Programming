def fizz_buzz(n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

n =eval(input("Enter the number: "))
result_array = fizz_buzz(n)

for i, value in enumerate(result_array, 1):
    print(f"{i}: {value}")
