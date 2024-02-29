import re

def is_valid_number(s):
    pattern = re.compile(r'^[+-]?(\d+\.\d*|\.\d+|\d+)([eE][+-]?\d+)?$')
    match = pattern.match(s)
    return bool(match)

# Take user input for numbers
user_input = input("Enter a number: ")

# Check if the entered number is valid
if is_valid_number(user_input):
    print(f'{user_input} is a valid number.')
else:
    print(f'{user_input} is not a valid number.')
