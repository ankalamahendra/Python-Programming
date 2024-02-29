def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return abs(a*b)//gcd(a,b)

n=int(input("Enter N value: "))
n1=eval(input("Enter N1 value: "))
n2=eval(input("Enter N2 value: "))

lcm_result=lcm(n1,n2)
gcd_result=gcd(n1,n2)

print(f"LCM={lcm_result}")
print(f"GCD={gcd_result}")
