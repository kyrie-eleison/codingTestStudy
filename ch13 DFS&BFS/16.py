#first, I have no idea, so I just tried BF.

import copy
from itertools import combinations

def solution(array):
    
    virus = []
    zeros = []
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 2:
                virus.append((i,j))
            if array[i][j] == 0:
                zeros.append((i,j))
    
    wallCandi = list(combinations(zeros, 3))
    answerCandi = []

    for walls in wallCandi:
        array_v = copy.deepcopy(array)
        for wall in walls:
            array_v[wall[0]][wall[1]] = 1
        
        for v in virus:
            dfs(array_v, v)

        answerCandi.append(findZeros(array_v))


    return max(answerCandi)


def dfs(array, start):

    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    x, y = start[0], start[1]
    array[x][y] = 2

    for move in moves:
        x_new, y_new = (x + move[0]), (y + move[1])

        if ((0 <= x_new <= len(array)-1) and (0 <= y_new <= len(array[0])-1)) and array[x_new][y_new] == 0:
            dfs(array, (x_new, y_new))

    
def findZeros(array):
    
    answer = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 0:
                answer += 1

    return answer

array = [[0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 2],
[1, 1, 1, 0, 0, 2],
[0, 0, 0, 0, 0, 2]]