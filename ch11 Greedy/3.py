def solution(array):

    current = array[0]
    change = 0
    for i in range(1, len(array)):
        if array[i] != current:
            current = array[i]
            change += 1
            
    if change%2 == 0:
        return int(change/2)
    else:
        return change//2 + 1

# https://www.acmicpc.net/problem/1439




