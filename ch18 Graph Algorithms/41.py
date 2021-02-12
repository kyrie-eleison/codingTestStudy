def root_finder(graph, parent, node):
  if parent[node] != node:
    parent[node] = root_finder(graph, parent, parent[node])
  
  return parent[node]

def union(graph, parent, a, b):
  rootA = root_finder(graph, parent, a)
  rootB = root_finder(graph, parent, b)

  if rootA <= rootB:
    parent[rootB] = rootA
  else:
    parent[rootA] = rootB

def solution(graph, trip):

  n = len(graph)
  parent = [0]*(n+1)
  
  for i in range(n):
    parent[i+1] = i+1

  for i in range(n):
    for j in range(n):
      if graph[i][j] == 1:
        union(graph, parent, i+1, j+1)
  
  for i in range(len(trip)-1):
    a, b = trip[i], trip[i+1]
    rootA = root_finder(graph, parent, a)
    rootB = root_finder(graph, parent, b)

    if rootA != rootB:
      return "No"

  return "Yes"

graph = [[0]*5 for _ in range(5)]
ones = [(0, 1), (0, 3), (0, 4), (1, 0), (1, 2), (1, 3), (2, 1), (3, 0), (3, 1), (4, 0)]

for one in ones:
  graph[one[0]][one[1]] = 1

trip = [2,3,4,3]

print(solution(graph, trip))
  
