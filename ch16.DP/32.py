def solution(triangle):
    d = [0]*len(triangle)
    d[0] = triangle[0]

    for i in range(1, len(triangle)):
        current = triangle[i]
        before = d[i-1]
        candi = [0]*(i+1)

        candi[0] = before[0] + current[0]
        candi[i] = before[i-1] + current[i]

        for j in range(1, i):
            candi[j] = max(before[j-1], before[j]) + current[j]
        
        d[i] = candi

    return max(d[-1])