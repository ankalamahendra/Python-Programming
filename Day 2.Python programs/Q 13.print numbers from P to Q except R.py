def print_numbers_except_digit(P, Q, R):
    result = []
    for num in range(P, Q + 1):
        if str(R) not in str(num):
            result.append(num)

    print("Numbers are =", ", ".join(map(str, result)))
    
P = eval(input("Enter P value: "))
Q = eval(input("Enter Q value: "))
R = eval(input("enter R value: "))

print_numbers_except_digit(P, Q, R)
