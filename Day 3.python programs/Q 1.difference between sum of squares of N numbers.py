
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

def square_of_sum(n):
    return sum(range(1, n+1))**2

def main():
    n =eval(input("Enter N value: "))
    sum_squares_result = sum_of_squares(n)
    square_sum_result = square_of_sum(n)

    difference = square_sum_result - sum_squares_result

    print(f"The sum of the squares of the first {n} natural numbers is: {sum_squares_result}")
    print(f"The square of the sum of the first {n} natural numbers is: {square_sum_result}")
    print(f"Hence, the difference is: {difference}")

if __name__ == "__main__":
    main()
