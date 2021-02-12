def solution(n, m, array):
    minList = []
    for i in range(n):
        nthRow = array[i*m:(i+1)*m]
        minList.append(min(nthRow))

    return max(minList)