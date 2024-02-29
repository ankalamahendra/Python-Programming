def max_guests_at_instance(T, entering, leaving):
    events = []
    for i in range(len(entering)):
        events.append((entering[i], 1)) 
        events.append((leaving[i], -1)) 

    events.sort()

    current_guests = 0
    max_guests = 0

    for event in events:
        current_guests += event[1]
        max_guests = max(max_guests, current_guests)

    return max_guests

def main():
    T = eval(input("Enter the value of T: "))
    
    entering = [eval(input("Enter number of guests entering at hour {}: ".format(i))) for i in range(T)]
    leaving = [eval(input("Enter number of guests leaving at hour {}: ".format(i))) for i in range(T)]

    result = max_guests_at_instance(T, entering, leaving)
    
    print(f"Maximum number of guests on cruise at an instance: {result}")

if __name__ == "__main__":
    main()
