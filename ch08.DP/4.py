d = [0]*1001

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    
    d[0], d[1] = 1,3

    x = 3
    while x <= n:
        d[x-1] = d[x-2] + 2*d[x-3]
        x += 1

    return d[n-1]