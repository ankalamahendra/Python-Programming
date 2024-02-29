def find_mth_max_and_nth_min(array, M, N):
    sorted_array = sorted(array, reverse=True)  # Sort array in descending order
    mth_max = sorted_array[M - 1]

    sorted_array = sorted(array)  # Sort array in ascending order
    nth_min = sorted_array[N - 1]

    return mth_max, nth_min

# Sample Input
array =eval(input("enter array elements: "))
M = eval(input("Enter M element: "))
N = eval(input("Enter N element: "))

# Output
mth_max, nth_min = find_mth_max_and_nth_min(array, M, N)
sum_result = mth_max + nth_min
difference_result = mth_max - nth_min

print(f"1st Maximum Number = {mth_max}")
print(f"3rd Minimum Number = {nth_min}")
print(f"Sum = {sum_result}")
print(f"Difference = {difference_result}")
