def count_sorted_vowel_strings(n):
  
    dp = [[0] * 5 for _ in range(n + 1)]

    for j in range(5):
        dp[1][j] = 1

    for i in range(2, n + 1):
        for j in range(5):
        
            dp[i][j] = sum(dp[i - 1][:j + 1])

    result = sum(dp[n])

    return result

n = int(input("Enter the length of the string: "))
result_count = count_sorted_vowel_strings(n)
print("Number of lexicographically sorted vowel strings of length", n, ":", result_count)
