def solution(consulting):
    dpTable = [0]* 21

    for i in range(len(consulting)):
        (t,p) = consulting[i]
        nextDay = i + t
        dpTable[nextDay] = max((p + dpTable[i]), dpTable[nextDay])
        
        dpTable[i+1] = max(dpTable[i], dpTable[i+1])
    
    
    return dpTable[len(consulting)]