def delchar(s, c):
    if len(c) != 1:
        return s
    
    result = ''
    for char in s:
        if char != c:
            result += char
    
    return result

input_string = input("Enter the string: ")
char_to_delete = input("Enter a character to be deleted: ")

result_string = delchar(input_string, char_to_delete)
print("String after the character is removed:", result_string)
