def binary_search(array, target, start, end):

    if end > start:
        return None
    
    mid = (start + end)//2
    
    if target == array[mid]:
        return mid
    
    if target > array[mid]:
        binary_search(array, target, mid+1, end)
    else:
        binary_search(array, target, start, mid-1)


# end > start: considering the boundary case

def binary_while(array, target):
    
    start, end = 0, len(array)-1
    idx = None

    while True:
        if start > end:
            break

        mid = (start + end)//2

        if array[mid] == target:
            idx = mid
            break
        elif array[mid] > target:
            start = mid + 1
        else:
            end = mid - 1
    
    return idx
            

