Infty = int(10e9)

graph = [[Infty]*(6) for _ in range(6)]
for (i,j) in [(1,2), (1,3), (1,4), (2,4), (3,4), (3,5), (4,5)]:
    graph[i][j] = 1
    graph[j][i] = 1
for i in range(6):
    graph[i][i] = 0

def solution(x, k, graph):
    #FM Algorithm
    table = graph
    n = len(graph)-1

    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                D_jk, D_ji, D_ik = graph[j][k], graph[j][i], graph[i][k]
                graph[j][k] = min(D_jk, D_ji + D_ik)

    cost = graph[1][k] + graph[k][x]
    
    if cost < Infty:
        return cost
    else:
        return -1

                


