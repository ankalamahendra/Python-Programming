def roman_to_integer(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    result = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_dict[char]

        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result

roman_numeral = input("Enter the Roman numeral: ")
integer_value = roman_to_integer(roman_numeral)
print("Integer representation:", integer_value)
