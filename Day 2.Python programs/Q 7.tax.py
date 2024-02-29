def calculate_tax(income):
    if income <= 150000:
        return 0
    elif income <= 300000:
        return 0.1 * (income - 150000)
    elif income <= 500000:
        return 0.2 * (income - 300000) + 0.1 * (300000 - 150000)
    else:
        return 0.3 * (income - 500000) + 0.2 * (500000 - 300000) + 0.1 * (300000 - 150000)

income = float(input("Enter the income: "))

tax = calculate_tax(income)
print("Tax =", tax)
