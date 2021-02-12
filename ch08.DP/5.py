d = [10001]*10001
def solution(array, n):
    for num in array:
        d[num-1] = 1
    
    x = max(array) + 1
    while x <= n:
        candidates = [d[x-j-1] for j in array]
        d[x-1] = min(candidates) + 1
        x += 1

    if d[n-1] >= 10001:
        return -1
    else:
        return d[n-1]