def is_scramble(s1, s2):
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        return False
    if s1 == s2:
        return True
    n = len(s1)
    for i in range(1, n):
        if (is_scramble(s1[:i], s2[:i]) and is_scramble(s1[i:], s2[i:])) or \
           (is_scramble(s1[:i], s2[-i:]) and is_scramble(s1[i:], s2[:-i])):
            return True
    return False

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

result = is_scramble(s1, s2)

if result:
    print("s2 is a scrambled string of s1.")
else:
    print("s2 is not a scrambled string of s1.")
