def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result_string = ''.join(char for char in input_string if char not in vowels)
    return result_string

user_input = input("Enter a string: ")

result = remove_vowels(user_input)
print(f"The string without vowels is: {result}")
