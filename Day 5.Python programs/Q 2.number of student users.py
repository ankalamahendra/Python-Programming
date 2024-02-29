def calculate_users(total_users, staff_users):
    
    student_users = total_users - staff_users

    non_teaching_staff_users = staff_users // 3

    return student_users, non_teaching_staff_users

total_users_input = int(input("Total Users: "))
staff_users_input = int(input("Staff Users: "))

student_users_result, non_teaching_staff_result = calculate_users(total_users_input, staff_users_input)

print("Sample Output:")
print(f"Student Users: {student_users_result}")
