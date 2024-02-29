def calculate_square_and_cube(number):
    
    square = number ** 2
    cube = number ** 3

    return square, cube

input_number =eval(input("Enter the number: "))
square_result, cube_result = calculate_square_and_cube(input_number)

print("Input: ",input_number)
print("Square: ",square_result)
print("Cube: ",cube_result)
