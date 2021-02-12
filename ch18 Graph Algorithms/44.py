n = 5
points = [(11, -15, -15), (14, -5, -15), (-1, -1, -5), (10, -4, -1), (19, -4, 19)]

num_set = set([i for i in range(n)])
graph = [[] for _ in range(n)]

for i in range(n):
  others = num_set - {i}
  x, y, z = points[i]
  for j in others:
    a, b, c = points[j]
    graph[i].append((j, min(abs(x-a), abs(y-b), abs(z-c))))


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
  
def is_cycle(graph, parent, a, b):
  rootA = root_finder(graph, parent, a)
  rootB = root_finder(graph, parent, b)

  if rootA == rootB:
    return True
  else:
    return False


from heapq import *

def solution(graph, n):

  answer = 0
  
  heap = []
  for i in range(n):
    connected_nodes = graph[i]
    
    for (j, w) in connected_nodes:
      heappush(heap, (w, i, j))

  parent = [0]*(n)
  for i in range(n):
    parent[i] = i

  while heap:

    next_least_edge = heappop(heap)
    w, i, j = next_least_edge

    if not is_cycle(graph, parent, i, j):
      union(graph, parent, i, j)
      answer += w
    else:
      continue

  return answer


print(solution(graph, n))

