def smaller_numbers_than_current(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result

nums =eval(input("Enter the array numbers: "))
result_list = smaller_numbers_than_current(nums)

print(result_list)
