def create_tuples(lower_range, upper_range):
    tuples_list = [(num, num**2) for num in range(lower_range, upper_range + 1)]
    return tuples_list

# Example usage:
lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))

result = create_tuples(lower_range, upper_range)
print("Result:", result)
