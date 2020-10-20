def solution(array, m, k):

    List = sorted(array)
    first = List[-1]
    second = List[-2]

    if first == second:
        return List[-1]*m
    else:
        return (m//(k+1))*(first*k + second) + (m%(k+1))*first