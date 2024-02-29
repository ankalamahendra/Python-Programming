def binary_to_decimal(binary_str):
    decimal_value = 0
    power = len(binary_str) - 1

    for digit in binary_str:
        if digit == '1':
            decimal_value += 2 ** power
        power -= 1

    return decimal_value

def find_maximum_binary(binary1, binary2, binary3):
    decimal1 = binary_to_decimal(binary1)
    decimal2 = binary_to_decimal(binary2)
    decimal3 = binary_to_decimal(binary3)

    maximum_decimal = max(decimal1, decimal2, decimal3)
    maximum_binary = bin(maximum_decimal)[2:]

    return maximum_binary

# Example usage
binary_value1 = "1101"
binary_value2 = "1010"
binary_value3 = "111"

maximum_binary_value = find_maximum_binary(binary_value1, binary_value2, binary_value3)

print("Binary values:", binary
