#Longest Increasing Sequence
#See: https://leetcode.com/problems/longest-increasing-subsequence/
#Also: https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

def solution(array):
    d = [0]*(len(array) + 1)

    d[1] = 1
    x = 2
    while x <= len(array):
        candi = []
        for i in range(1, x):
            if array[i-1] >= array[x-1]:
                candi.append(d[i])
 
        if candi:
            d[x] = max(candi) + 1
        else:
            d[x] = 1

        x += 1

    LIS = max(d)

    return len(array) - LIS