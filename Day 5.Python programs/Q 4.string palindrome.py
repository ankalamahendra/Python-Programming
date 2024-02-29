def isPalindrome(s):
    s = s.lower()

    s = ''.join(char for char in s if char.isalnum())

    return s == s[::-1]

input_string = eval(input("Enter the string: "))
result = isPalindrome(input_string)
print(result)
