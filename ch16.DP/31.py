def solution(array, n, m):
    
    matrix = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrix[i][j] = array[i + m*j]
    
    d = [0]*(m+1)
    d[0] = matrix[0]
    
    for i in range(1, m):
        a_i = [0]*n
        a_before = d[i-1]
        a_i[0] = max(a_before[0], a_before[1]) + matrix[i][0]
        a_i[n-1] = max(a_before[n-2], a_before[n-1]) + matrix[i][n-1]
        
        for j in range(1, n-1):
            a_i[j] = max(a_before[j-1], a_before[j], a_before[j+1]) + matrix[i][j]
        
        d[i] = a_i
    
    return max(d[m-1])