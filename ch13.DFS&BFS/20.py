from itertools import combinations
import copy

def solution(array):
    n = len(array)

    teacher = []
    obsCandi = []
    student = []
    for i in range(n):
        for j in range(n):
            if array[i][j] == "T":
                teacher.append((i,j))
            if array[i][j] == "X":
                obsCandi.append((i,j))
            if array[i][j] == "S":
                student.append((i,j))


    obsCandi_list = list(combinations(obsCandi, 3))
    
    for obs in obsCandi_list:
        array_obs = copy.deepcopy(array)
        for o in obs:
            array_obs[o[0]][o[1]] = "O"

        for t in teacher:
            contamination(array_obs, t)

        for s in student:
            if array_obs[s[0]][s[1]] == "S":
                return True

    return False


def contamination(array, t):
    
    n = len(array)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    x, y = t[0], t[1]
    
    for move in moves:
        x_new, y_new = x + move[0], y + move[1]


        while (0 <= x_new <= (n-1)) and (0 <= y_new <= (n-1)):


            if array[x_new][y_new] == "O":
                break

            else:
                array[x_new][y_new] = "T"
                x_new += move[0]
                y_new += move[1]
                continue

            
        

array = [["X","S","X","X","T"],  ["T","X","S","X","X"], ["X","X","X","X","X"], ["X","T","X","X","X"], ["X","X","T","X","X"]]

array2 = [["S", "S", "S", "T"], ["X","X","X","X"], ["X","X","X","X"], ["T", "T", "T", "X"]]

print(solution(array2))