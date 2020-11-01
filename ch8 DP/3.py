d = [0]*101

def solution(array):
    
    if len(array) == 1:
        return array[0]
    
    else:
        d[0] = array[0]
        if len(array) == 2:
            d[1] = array[1]
        else:
            d[1] = array[1]
            d[2] = array[0] + array[2]

    x = 4    
    while x <= len(array):
        d[x-1] = max(d[x-3], d[x-4]) + array[x-1]
        x += 1
    
    return max(d[x-1], d[x-2])

#textbook's solution(concentrating on the direct solution)

def solution2(array):

    if len(array) == 1:
        return array[0]

    d[0], d[1] = array[0], array[1]

    x = 3

    while x <= len(array):
        d[x-1] = max(d[x-2], d[x-3]+array[x-1])
        x += 1

    return d[len(array)-1] 

    