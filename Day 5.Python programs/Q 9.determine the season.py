def get_season(month, day):
    month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                  'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

    month_num = month_dict[month]

    if (month_num == 3 and day >= 20) or (month_num == 4 or month_num == 5) or (month_num == 6 and day < 21):
        return "Spring"
    elif (month_num == 6 and day >= 21) or (month_num == 7 or month_num == 8) or (month_num == 9 and day < 22):
        return "Summer"
    elif (month_num == 9 and day >= 22) or (month_num == 10 or month_num == 11) or (month_num == 12 and day < 21):
        return "Fall"
    else:
        return "Winter"

input_month = input("Enter the month: ")
input_day = int(input("Enter the day: "))

season = get_season(input_month, input_day)
print(f"The season for {input_month} {input_day} is {season}.")
