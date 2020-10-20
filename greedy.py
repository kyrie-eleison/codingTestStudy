def solution(List, m, k):
    answer = 0

    n = len(List)
    List = sorted(List)

    if List[-1] == List[-2]:
        return List[-1]*n
    else:
        

    