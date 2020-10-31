#First, I thought of sequential search. But it is rather inefficient
#So we use binary search instead:

#Bad example(which I thought first)
def solution(array, length):
    maxVal = max(array)
    level = maxVal - length
    left = []
    answer = 0

    while True:
        for i in range(len(array)):
            if array[i]-level > 0:
                left.append(array[i]-level)
        
        if sum(left) >= length:
            level += 1
            left = []
        else:
            break
            
    return level - 1

#Using binary search(in the textbook)

def solution2(array, length):
    start = 0
    end = max(array)

    
    while start <= end:
        mid = (start + end)//2
        total = 0 
        
        for i in range(len(array)):
            if array[i] - mid > 0:
                total += array[i] - mid
        
        if total == length:
            return mid
        elif total > length:
            start = mid + 1
        else:
            end = mid - 1
    
    return mid






