def create_tuple_list(lower, upper):
    result = [(num, num**2) for num in range(lower, upper + 1)]
    return result

lower_range = int(input("Enter the lower range value: "))
upper_range = int(input("Enter the upper range value: "))

output_list = create_tuple_list(lower_range, upper_range)
print(output_list)
