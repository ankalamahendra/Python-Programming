def is_palindrome(s):
    return s == s[::-1]

def is_number_palindrome(num):
    num_str = str(num)
    return is_palindrome(num_str)

# Sample Input
choice = int(input("Enter your choice (1 for string, 2 for number): "))

if choice == 1:
    # Checking for Palindrome String
    input_string = input("Enter the string: ")
    if is_palindrome(input_string):
        print("Palindrome")
    else:
        print("Not a Palindrome")
elif choice == 2:
    # Checking for Palindrome Number
    input_number = int(input("Enter the number: "))
    if is_number_palindrome(input_number):
        print("Palindrome")
    else:
        print("Not a Palindrome")
else:
    print("Invalid choice. Please enter 1 for string or 2 for number.")
