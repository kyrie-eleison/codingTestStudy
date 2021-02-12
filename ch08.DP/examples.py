#top-down(memoization): using recursion
d = [0]*100
def fibo(n):
    print("called", n)
    if n <= 2:
        return 1

    if d[n] != 0:
        return d[n]

    else:
        d[n] = fibo(n-1) + fibo(n-2)
        return d[n]
#bottom-up
d = [0]*100
def fibo2(n):
    if n <= 2:
        return 1
    
    d[0], d[1] = 1, 1
    x = 3    

    while x <= n:
        d[x] = d[x-1] + d[x-2]
        x += 1
    
    return d[n]




    