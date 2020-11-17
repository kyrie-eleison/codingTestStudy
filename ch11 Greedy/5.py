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
        
        print("(i,j): ", (i,j))
        ballA = j - i
        ballB = n - j
        answer += ballA*ballB
        print(answer)
        i = j
        print("###")
        
    
    return answer         