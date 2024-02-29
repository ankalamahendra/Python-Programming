def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def find_anniversary_year(year):
    if is_leap_year(year):
        print(f"{year} is a leap year. The next anniversary year is {year + 4}.")
    else:
        print(f"{year} is not a leap year. The previous anniversary year is {year - 4}.")

# Example usage:
anniversary_year = int(input("Enter the anniversary year: "))
find_anniversary_year(anniversary_year)
