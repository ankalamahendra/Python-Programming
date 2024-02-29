def min_jumps_to_end(nums):
    n = len(nums)

    if n == 0 or nums[0] == 0:
        return -1 

    jumps = 0
    max_reach = nums[0]  
    steps_left = nums[0]  

    for i in range(1, n):
        if i == n - 1:
            return jumps  

        max_reach = max(max_reach, i + nums[i])
        steps_left -= 1

        if steps_left == 0:
            jumps += 1

            if i >= max_reach:
                return -1  

            steps_left = max_reach - i

    return -1

nums =eval(input("Enter the array numbers: "))
result = min_jumps_to_end(nums)
print(result)
