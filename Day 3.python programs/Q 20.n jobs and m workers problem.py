def max_profit(difficulty, profit, worker):
    jobs = sorted(zip(difficulty, profit))
    worker=sorted(list(worker))
    
    total_profit = 0
    i = 0  

    for w in worker:
        while i < len(jobs) and jobs[i][0] <= w:
            i += 1

        if i > 0:
            total_profit += max(j[1] for j in jobs[:i])

    return total_profit

difficulty =eval(input("Enter difficulty array numbers: "))
profit =eval(input("Enter profit array numbers: ")) 
worker =eval(input("Enter worker array numbers: "))

result = max_profit(difficulty, profit, worker)
print(f"Maximum profit: {result}")
