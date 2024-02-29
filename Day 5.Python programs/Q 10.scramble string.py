def isScramble(s1, s2):
    if s1 == s2:
        return True

    if len(s1) != len(s2):
        return False

    if sorted(s1) != sorted(s2):
        return False

    n = len(s1)

    memo = {}

    def helper(s1, s2):
        if (s1, s2) in memo:
            return memo[(s1, s2)]

        if s1 == s2:
            memo[(s1, s2)] = True
            return True

        for i in range(1, n):
            if (helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:])) or \
               (helper(s1[:i], s2[-i:]) and helper(s1[i:], s2[:-i])):
                memo[(s1, s2)] = True
                return True

        memo[(s1, s2)] = False
        return False

    return helper(s1, s2)

s1 = eval(input("Enter the S1 string: "))
s2 = eval(input("Enter the S2 string: "))
result = isScramble(s1, s2)
print(result)
