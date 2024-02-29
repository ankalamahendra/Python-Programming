def is_perfect_square(num):
    root = int(num**0.5)
    return num == root**2

def sum_of_digits_less_than_10(num):
    return sum(int(digit) for digit in str(num)) < 10

def main():
    lower_range = int(input("Enter lower range: "))
    upper_range = int(input("Enter upper range: "))

    result_list = [num for num in range(lower_range, upper_range + 1) if is_perfect_square(num) and sum_of_digits_less_than_10(num)]

    print(result_list)

if __name__ == "__main__":
    main()
