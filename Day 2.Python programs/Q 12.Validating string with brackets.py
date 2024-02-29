def isValid(s):
    stack=[]
    bracket_mapping={')':'(','}':'{',']':'['}

    for char in s:
        if char in bracket_mapping.values():
            stack.append(char)
        elif char in bracket_mapping.keys():
            if not stack or bracket_mapping[char] !=stack.pop():
                return False
        else:
            return False

    return not stack

input_string=eval(input("enter the string: "))
result=isValid(input_string)
print(result)
                
            
                
