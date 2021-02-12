array = [[1,0,2], [0,0,0,], [3,0,0]]
s, x, y, = 2, 3, 2
from heapq import *

def solution(array, s, x_answer, y_answer):

    second = 0
    BFS = []

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] != 0:
                BFS.append((array[i][j], i, j))
    
    while second < s:
        bfs_len = len(BFS)
        BFS.sort()

        for _ in range(bfs_len):
            current_node = BFS.pop(0)
            vtype, x, y = current_node

            if x < len(array) - 1:
                x_d, y_d = x+1, y
                if array[x_d][y_d] == 0:
                    array[x_d][y_d] = vtype
                    BFS.append((vtype, x_d, y_d))
            if x > 0:
                x_u, y_u = x-1, y
                if array[x_l][y_l] == 0:
                    array[x_l][y_l] = vtype
                    BFS.append((vtype, x_u, y_u))
            
            if y < len(array[0]) - 1:
                x_r, y_r = x, y+1
                if array[x_r][y_r] == 0:
                    array[x_r][y_r] = vtype
                    BFS.append((vtype, x_r, y_r))

            if y > 0:
                x_l, y_l = x, y-1
                if array[x_l][y_l] == 0:
                    array[x_][y_l] = vtype
                    BFS.append((vtype, x_l, y_l))
                    

        second += 1
        print(array)
    
    return array[x_answer-1][y_answer-1]