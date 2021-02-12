INF = int(10e9)
graph = [[0, 2, 3, 1, 10], [INF, 0, INF, 2, INF], [8, INF, 0, 1, 1], [INF, INF, INF, 0, 3], [7, 4, INF, INF, 0]]

def fw(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == INF:
                graph[i][j] = 0
    
    return graph

print(fw(graph))