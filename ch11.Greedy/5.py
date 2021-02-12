def solution(array):
    i,j = 0,0
    array = sorted(array)
    n = len(array)
    answer = 0
    
    while i <= (n-1):
        while array[i] == array[j]:
            j += 1
            if j >= n:
                break
        
        ballA = j - i
        ballB = n - j
        answer += ballA*ballB

        i = j
        
    
    return answer         

#textbook solution
def solution2(array):

    d = [0]*(max(array)+1)
    n = len(array)
    answer = 0
    for num in array:
        d[array] += 1

    for i in range(1, len(d)):
        n -= d[i] #for B
        answer += n*d[i]

    return answer 



