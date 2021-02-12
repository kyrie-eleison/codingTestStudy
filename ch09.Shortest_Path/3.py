from heapq import *
Infty = int(10e9)
n = 3
graph = [[] for _ in range(n+1)]
graph[1].append((2,4))
graph[1].append((3,2))

def solution(start, graph):
    #Dijkstra
    n = len(graph)-1
    distance = [Infty]*(n+1)
    distance[start] = 0


    heap = [(0,start)]

    while heap:
        print(heap)
        print(distance)
        curr_dist, curr_node = heappop(heap)
        if curr_dist > distance[curr_node]:
            continue

        for (node, dist) in graph[curr_node]:
            cost = dist + distance[curr_node]
            if cost < distance[node]:
                distance[node] = cost
                heappush(heap, (cost, node))
    print(distance)

    answer = []
    for i in range(1, n+1):
        node_i_dist = distance[i]
        if 0 < node_i_dist < Infty:
            answer.append(node_i_dist)
    
    return len(answer), max(answer)




