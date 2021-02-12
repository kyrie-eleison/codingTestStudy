def solution(ice):

    answer = 0

    def dfs(graph, v):
        x,y = v
        graph[x][y] = 1
        dx = [-1, 1, 0 ,0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (-1 < nx < len(graph)) and (-1 < ny < len(graph[0])):
                if graph[nx][ny] == 0:
                    v = (nx, ny)
                    dfs(graph, v)

    for i in range(len(ice)):
        row = ice[i]
        for j in range(len(row)):
            if row[i] == 0:
                answer += 1
                dfs(ice, (i,j))

    return answer








ice = [[0,0,1,1,0],[0,0,0,0,0], [1,1,1,1,1], [0,0,0,0,0]]

