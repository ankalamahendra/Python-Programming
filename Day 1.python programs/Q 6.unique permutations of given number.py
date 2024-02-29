from itertools import permutations

def unique_permutations(num):
    num_str=str(num)

    unique_perms=set(permutations(num_str))
    for perm_tuple in unique_perms:
        perm_int=int(''.join(perm_tuple))
        print(perm_int)

input_number=input("enter any number: ")
print(input_number)
unique_permutations(input_number)
        
