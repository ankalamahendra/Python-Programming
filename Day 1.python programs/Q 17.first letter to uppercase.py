input_string =input("Enter the any string: ")

output_string = '.'.join(word.capitalize() for word in input_string.split())

print("Input:", input_string)
print("Output:", output_string)
