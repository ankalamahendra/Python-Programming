def is_perfect_square(num):
    square_root = int(num**0.5)
    return square_root**2 == num

def sum_of_digits_less_than_10(num):
    digit_sum = sum(map(int, str(num)))
    return digit_sum < 10

def perfect_squares_with_sum_less_than_10(lower, upper):
    result = [num for num in range(lower, upper + 1) if is_perfect_square(num) and sum_of_digits_less_than_10(num)]
    return result

lower_range = int(input("Enter lower range: "))
upper_range = int(input("Enter upper range: "))

output_list = perfect_squares_with_sum_less_than_10(lower_range, upper_range)
print(output_list)
