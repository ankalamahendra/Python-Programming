def find_common_divisors(a, b):
    common_divisors = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_divisors.append(i)
    return common_divisors

numbers = input("Enter the integer values: ")
num_list = [int(num) for num in numbers.split(',')]

if len(num_list) == 2:
    common_divisors = find_common_divisors(num_list[0], num_list[1])
    print("Output:", common_divisors)
else:
    print("Invalid input ")
