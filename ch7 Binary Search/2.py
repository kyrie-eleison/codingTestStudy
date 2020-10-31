#using binary search
def binary_search(array, target, start, end):

    if start > end:
        return None
    
    mid = (start + end)//2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array,target, start, mid-1)

array = [8,3,7,9,2]

def solution(shop, demand):
    shop = sorted(shop)
    answer = []
    for num in demand:
        if binary_search(shop, num, 0, len(shop)-1) != None:
            answer.append("yes")
        else:
            answer.append("no")

    return answer

#using hash(dictionary)
def solution2(shop, demand):

    dic = dict()
    for num in shop:
        dic[num] = True
    answer = []

    for num in demand:
        try:
            if dic[num] == True:
                answer.append("yes")
            else:
                answer.append("no")
        except:
            answer.append("no")
            
    return answer


##textbook answer
#using count search

def solution3(shop, demand):

    minIdx = 0
    maxIdx = 0
    for i in range(len(shop)):
        num = shop[i]
        if shop[minIdx] > num:
            minIdx = i
        if shop[maxIdx] < num:
            maxIdx = i

    k = shop[maxIdx] - shop[minIdx] + 1
    array = [0]*k

    for num in shop:
        array[num-shop[minIdx]] += 1
    
    answer = []
    
    for num in demand:
        if array[num-shop[minIdx]] > 0:
            answer.append("yes")
        else:
            answer.append("no")

    return answer

#using set

def solution4(shop, demand):
    shop = set(shop)
    answer = []

    for num in demand:
        if num in shop:
            answer.append("yes")
        else:
            answer.append("no")

    return answer
            


