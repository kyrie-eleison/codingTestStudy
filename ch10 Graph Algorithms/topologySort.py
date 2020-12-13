#Code from the textbook(Implementing indegree array for fast reference)
from collections import deque

v = 7
edges = [(1,2), (1,5), (2,3), (2,6), (3,4), (4,7), (5,6), (6,4)]
graph = [[] for _ in range(v+1)]
indegree = [0]*(v+1)

for edge in edges:
    graph[edge[0]].append(edge[1])
    indegree[edge[1]] += 1


queue = deque()
for i in range(1, v+1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    currentNode = queue.popleft()
    result.append(currentNode)

    nextNodes = graph[currentNode]

    for node in nextNodes:
        indegree[node] -= 1
        
        if indegree[node] == 0:
            queue.append(node)
    
