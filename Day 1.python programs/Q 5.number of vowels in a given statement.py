def count_vowels(statement):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    count=0

    for char in statement:
        if char in vowels:
            count=count+1

    return count
input_statement=input("enter the input statement: ")
num_vowels=count_vowels(input_statement)
print(num_vowels)
