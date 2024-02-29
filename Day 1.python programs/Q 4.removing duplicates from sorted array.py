def remove_duplicates(arr):
    unique_arr=[]
    for num in arr:
        if num not in unique_arr:
            unique_arr.append(num)

    return unique_arr
input_array=eval(input("Enter the array numbers: "))
result=remove_duplicates(sorted(input_array))
print(result)
            
