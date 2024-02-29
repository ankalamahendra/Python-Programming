input_string=input("enter any string")
vowels="aeiouAEIOU"
string_without_vowels=''.join(char for char in input_string if char not in vowels)
print(string_without_vowels)
