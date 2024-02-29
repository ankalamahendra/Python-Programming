def my_func(x):
    if x<0:
        return 1
    return x * my_func(x-1)
x=int(input("Enter the number: "))
print(my_func(x))
