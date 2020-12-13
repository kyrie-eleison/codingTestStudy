def solution(array, n):
    start = 0
    array.sort()
    end = (array[-1] - array[0])//(n-1)
    answer = 0

    while start <= end:
        mid = (start + end)//2
        

        if possible(array, mid, n):
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer


def possible(array, length, n):
    i = 0
    acc = 0
    current_elt = array[i]
    while i < len(array)-1:
        next_elt = array[i+1]
        if next_elt < length + current_elt:
            i += 1
        else:
            current_elt = next_elt
            acc += 1
            if acc >= n-1:
                return True
            
    return False

