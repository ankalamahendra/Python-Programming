def evaluate_expression(s):
    stack = []
    num = 0
    sign = '+'
    operators = {'+', '-', '*', '/'}
    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)
        if char in operators or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] *= num
            elif sign == '/':
                stack[-1] = int(stack[-1] / num)  
            num = 0
            sign = char
    return sum(stack)

expression = input("Enter the expression: ")

result = evaluate_expression(expression.replace(" ", ""))

print("Result:",result)
