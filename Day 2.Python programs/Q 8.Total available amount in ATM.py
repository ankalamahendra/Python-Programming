def calculate_total_balance(denominations, notes):
    total_balance = sum(denomination * note for denomination, note in zip(denominations, notes))
    return total_balance

# Sample Input
denomination_1 = int(input("Enter the 1st Denomination: "))
notes_1 = int(input(f"Enter the 1st Denomination number of notes: "))
denomination_2 = int(input("Enter the 2nd Denomination: "))
notes_2 = int(input(f"Enter the 2nd Denomination number of notes: "))
denomination_3 = int(input("Enter the 3rd Denomination: "))
notes_3 = int(input(f"Enter the 3rd Denomination number of notes: "))
denomination_4 = int(input("Enter the 4th Denomination: "))
notes_4 = int(input(f"Enter the 4th Denomination number of notes: "))

# Denomination priority based on user input
denominations = [denomination_1, denomination_2, denomination_3, denomination_4]
notes = [notes_1, notes_2, notes_3, notes_4]

# Output
total_balance = calculate_total_balance(denominations, notes)
print("Total Available Balance in ATM:", total_balance)
