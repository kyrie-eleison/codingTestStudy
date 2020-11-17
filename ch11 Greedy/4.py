from itertools import combinations

def solution(array):
    d = [0]*max(array)*2
    
    for i in range(len(array)):
        candis = combinations(array, i+1)
        for tup in candis:
            d[sum(tup)] = 1
            
    for j in range(1, len(d)):
        if d[j] == 0:
            return j