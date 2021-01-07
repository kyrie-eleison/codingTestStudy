import copy

def solution(array, L, R):
    answer = 0
    for i in range(len(array)):
        for j in range(len(array)):
            array[i][j] = (array[i][j], (i,j))

    while True:
        array_i = copy.deepcopy(array)
        cluster_list = []
        isOpen = False
        visited = [[False]*len(array) for _ in range(len(array))]
        for i in range(len(array)):
            for j in range(len(array)):
                if visited[i][j] == False:
                    (cluster, open) = openDoor(array_i, (i,j), L, R, [], False, visited)
                    if open:
                        answer += 1
                        isOpen = True
                        cluster_list.append(cluster)

        if not isOpen:
            return answer

        for cluster in cluster_list:
            together(array, cluster)
        print("#####")
        print(array)


    return answer

def openDoor(array, start, L, R, answer, open, visited):

    answer += [start]
    x, y = start
    visited[x][y] = True

    moves = [(0,1), (0,-1), (1,0), (-1,0)]

    for move in moves:
        x_new, y_new = x + move[0], y + move[1]

        if (0 <= x_new <= len(array)-1) and (0 <= y_new <= len(array)-1):
            
            if visited[x_new][y_new] == False:

                if L <= abs(array[x_new][y_new][0] - array[x][y][0]) <= R:
                    visited[x_new][y_new] = True
                    (answer, open) = openDoor(array, (x_new, y_new), L, R, answer, True, visited)

                if array[x_new][y_new][1] == array[x][y][1]:
                    visited[x_new][y_new] = True
                    (answer, open) = openDoor(array, (x_new, y_new), L, R, answer, open, visited)

    return (answer, open)
    
def together(array_original, cluster):

    average = 0
    number = len(cluster)

    for node in cluster:
        average += array_original[node[0]][node[1]][0]

    average = average/number

    for node in cluster:
        array_original[node[0]][node[1]] = (average, cluster[0])


L, R = 20, 50
array = [[50, 30], [30, 40]]

print('answer: ')
print(solution(array, L, R))
