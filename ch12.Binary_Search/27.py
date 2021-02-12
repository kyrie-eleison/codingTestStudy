def binaryMore(array, target, start, end):
    if start > end:
        return 
    
    answer = 0
    while start <= end:
        mid = (start + end)//2
        print(mid)

        if array[mid] <= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer

def binaryLess(array, target, start, end):
    if start > end:
        return 
    
    answer = 0
    while start <= end:
        mid = (start + end)//2
        
        if array[mid] >= target:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer
        

def solution(array, target):
    n = len(array)

    start = binaryLess(array, target, 0, n-1)
    end = binaryMore(array, target, 0, n-1)
    
    
    if start == 0 or end == n-1:
        if array[start] != target or array[end] != target:
            return -1

    return (end - start) + 1
