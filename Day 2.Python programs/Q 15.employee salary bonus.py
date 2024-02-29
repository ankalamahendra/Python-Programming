def calculate_bonus(salary, grade):
    base_bonus_percentage = 0.05  
    extra_bonus_percentage = 0.02 
    if grade == 'B':
        base_bonus_percentage = 0.10  

    bonus = salary * base_bonus_percentage

    if salary < 10000:
        bonus += salary * extra_bonus_percentage

    total_salary = salary + bonus
    return bonus, total_salary


grade = input("Enter the grade of the employee: ")
salary = float(input("Enter the employee salary: "))

bonus, total_salary = calculate_bonus(salary, grade)

print(f"Salary = {salary}")
print(f"Bonus = {bonus}")
print(f"Total to be paid: {total_salary}")
