#Selection Sort
#A basic method for finding min/max value in an array
#O(n^2)
def select(array):

    for i in range(len(array)):
        minIdx = i
        for j in range(i+1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j

        array[minIdx], array[i] = array[i], array[minIdx]

    return array

#Insertion Sort -> rather call transposition rather than insert!
#Very powerful when the array is almost sorted already
#O(n^2)
def insert(array):

    if len(array) <= 1:
        return array

    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
            
    return array

#Quick Sort(with Hoare Partition(setting the first element as the pivot))
#Most renowned algorithm, which uses pivot
#O(nlogn) usually, but in worst O(n^2)
#The same code as the book
def quick_sort(array, start, end):
    if start>=end:
        return
    
    pivot = start
    left, right = start+1, end-1
    
    while left<=right:
        while left <= end-1 and array[left] <= array[pivot]:
            left += 1
        while right >= start + 1 and array[right] >= array[pivot]:
            right -= 1
        
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    
#Python function: call by reference -> but list slicing makes a new one.
#Always need to consider the boundary condition, especially for the recursion case.
#Try to write the code more intuitively!!!

def quick(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    
    left = [x for x in array[1:] if x < pivot]
    right = [x for x in array[1:] if x > pivot]
    middle= [x for x in array[1:] if x == pivot]
    
    return quick(left) + middle + [pivot] + quick(right)
    
#Count Sort
#When k = max - min is rather small
#O(n+k)
#not based on comparing methods

def count(array):
    
    minIdx = 0
    maxIdx = 0

    for k in range(len(array)):
        if array[k] < array[minIdx]:
            minIdx = k
        if array[k] > array[maxIdx]:
            maxIdx = k
    
    k = array[maxIdx] - array[minIdx]
    countList = [0]*(k+1)

    for num in array:
        countList[num] += 1

    returnArray = []
    for i in range(len(countList)):
        if countList[i] > 0:
            while countList[i] > 0:
                returnArray.append(i)
                countList[i] -= 1

    return returnArray

    