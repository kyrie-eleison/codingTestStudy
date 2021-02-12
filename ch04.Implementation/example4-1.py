#A bit different than the book's solution
#Book's one is more recommendable

def solution(n, plan):
    current = [1,1]

    while plan:
        command = plan.pop(0)
        if command == "R":
            current[1] += 1
            if current[1] > n: 
                current[1] = n
        
        if command == "L":
            current[1] += -1
            if current[1] < 1: 
                current[1] = 1
        
        if command == "U":
            current[0] += -1
            if current[0] < 1: 
                current[0] = 1
        
        if command == "D":
            current[0] += 1
            if current[0] > n: 
                current[0] = n
    
    return current

    #What would be a more elegant way of writing this kind of problem?


        
        

