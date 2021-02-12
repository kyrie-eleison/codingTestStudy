#DFS
def dfs(graph, v, visted):
    
    visited[v-1] = True
    print(v+1)
    
    adjoint = graph[v+1]

    for node in adjoint:
        if visited[node] == False:
            dfs(graph, node, visited)

def dfs2(graph, v):

    visited = [False]*8
    stack = [v]

    while stack:
        node = stack[-1]
        if visited[node-1] == False:
            print(node)
        visited[node-1] = True
        
        unvisited = False
        for adj in graph[node-1]:
            if visited[adj-1] == False:
                stack.append(adj)
                unvisited = True
                break
        
        if unvisited == False:
            stack.pop()


visited = [False]*8
    
graph = [[2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]

#BFS
from collections import deque

def bfs(graph, start):

    queue = deque([start])
    visited = [False]*len(graph)

    while queue:
        node = queue.popleft()
        if visited[node-1] == False:
            print(node)
            visited[node-1] = True

        for adj in graph[node-1]:
            if visited[adj-1] == False:
                queue.append(adj)


